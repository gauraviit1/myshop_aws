from django import template
from shop.models import Product
register = template.Library()


@register.filter(name='productfilter')
def productfilter(subcategory):
		products = subcategory.products.all().filter(parent_product__isnull=True)
		return products
