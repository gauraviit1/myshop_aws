from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from PIL import Image
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
import re
from mptt.models import MPTTModel, TreeForeignKey
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
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    features = JSONField(blank=True, null=True)

    class Meta:
        ordering = ['name']
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
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

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


class ModifiedProduct(MPTTModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    category = models.ForeignKey(ModifiedCategory, related_name = 'category')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="modifiedproducts/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    features = JSONField(blank=True, null=True)


    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
    class Meta:
        ordering = ['name']
        index_together = [('id', 'slug')]
        

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])