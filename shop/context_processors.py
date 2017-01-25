from shop.models import ModifiedCategory, ModifiedProduct


def bakery_items(request):
		bakery_item = ModifiedCategory.objects.get(name="Bakery").get_descendants()
		return {'bakery_item': bakery_item}


def handicraft_items(request):
		handicraft_item = ModifiedCategory.objects.get(name="Handicrafts").get_descendants()
		return {'handicraft_item': handicraft_item}

def all_unique_products(request):
		all_unique_products = ModifiedProduct.objects.filter(level=0)
		return {'all_unique_products': all_unique_products}