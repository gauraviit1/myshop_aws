from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
import re
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import mark_safe
# Create your models here.


class Cateogry(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(db_index=True, unique=True)
    parent_cateogry = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'cateogry'
        verbose_name_plural = 'cateogries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_cateogry', args=[self.slug])

    def save(self, *args, **kwargs):
        for field_name in ['name', ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Cateogry, self).save(*args, **kwargs)


class Product(models.Model):
    cateogry = models.ForeignKey('Cateogry', related_name='products')
    parent_product = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    features = JSONField(blank=True, null=True)

    class Meta:
        ordering = ['created']
        index_together = [('id', 'slug')]

    def __str__(self):
        return self.name

    def option_value(self):
        if self.parent_product:
            pattern = '(?<=\()(.*?)(?=\))'
            return re.search(pattern, self.name).group()

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def clean(self, *args, **kwargs):
        if self.parent_product:
            if not self.price:
                raise ValidationError('Price field cannot be empty')
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



# Create your models here.
class ModifiedCategory(MPTTModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(db_index=True, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ['name']
        verbose_name = 'modified category'
        verbose_name_plural = 'modified categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        for field_name in ['name', ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super().save(*args, **kwargs)

    def get_description(self):
        try:
            if self.description:
                return self.description
            else:
                return self.parent.get_description()
        except:
            pass



class ModifiedProduct(MPTTModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    category = models.ForeignKey(ModifiedCategory,
                                 related_name='category')
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    features = JSONField(blank=True, null=True)
    option_type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ['created']
        index_together = [('id', 'slug')]

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


    def get_features(self):
        try:
            if self.features:
                return self.features
            else:
                return self.parent.get_features()
        except:
            pass        

    def get_images(self):
        try:
            if self.product.all():
                return self.product.all()
            else:
                return self.parent.get_images()
        except:
            pass
 

    def get_description(self):
        try:
            if self.description:
                return self.description
            else:
                return self.parent.get_description()
        except:
            pass

    def get_option_name(self):
        try:
            pattern = '(?<=\()(.*?)(?=\))'
            return re.findall(pattern, self.name)[-1]
        except:
            pass

    def name_for_hierarchial_list(self):
        try:
            pattern = '(?<=\()(.*?)(?=\))'
            return re.findall(pattern, self.name)[-1]
        except:
            return self.name

    def get_options(self):
        options = self.get_ancestors().exclude(level=0)
        return options


class ProductImages(models.Model):
    image = models.ImageField(upload_to="modifiedproducts/images/%Y/%m/%d",
                              blank=True)
    product = models.ForeignKey(ModifiedProduct,
                                related_name="product")

    class Meta:
        verbose_name = 'images related with products'
        verbose_name_plural = 'Product Images'


    def __str__(self):
        return self.image.name

    def image_tag(self):
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))
