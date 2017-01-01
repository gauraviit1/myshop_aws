from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from PIL import Image
from django.contrib.postgres.fields import HStoreField

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

# Create your models here.
class Cateogry(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(db_index=True, unique=True)

    class Meta:
        ordering =   ['name']
        verbose_name = 'cateogry'
        verbose_name_plural = 'cateogries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_cateogry', args=[self.slug])

    def save(self, *args, **kwargs):
        for field_name in ['name',]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Cateogry, self).save(*args, **kwargs)


class Product(models.Model):
    cateogry = models.ForeignKey('Cateogry', related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [('id', 'slug')]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Attribute(models.Model):
    product = models.ForeignKey('Product', related_name="patt")
    weight = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    waist_size = models.PositiveSmallIntegerField(blank=True, null=True)
    size = models.CharField(max_length=2, blank=True, null=True)

    def clean(self, *args, **kwargs):
        super(Attribute, self).clean(*args, **kwargs)
        if self.weight == Decimal('0.350'):
            raise ValidationError({'weight': _('Cannot use this value')})

    class Meta:
        unique_together = ('product', 'weight')
