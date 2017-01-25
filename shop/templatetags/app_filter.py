from django import template
from shop.models import ModifiedProduct
register = template.Library()

@register.filter(name='filter2')
def filter2(category):
		products =ModifiedProduct.objects.filter(category=category)
		return products
