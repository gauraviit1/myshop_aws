from shop.models import Product


def bakery_items(request):
	bakery_items = Product.objects.filter(available=True, cateogry__name="Bakery")
	return {'bakery_items': bakery_items}


def handicraft_items(request):
	handicraft_items = Product.objects.filter(available=True, cateogry__name="Handicrafts")
	return {'handicraft_items': handicraft_items}
