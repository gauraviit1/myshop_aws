from shop.models import Product, Cateogry


def bakery_items(request):
		bakery_categories = Cateogry.objects.get(name="Bakery")
		bakery_categories = bakery_categories.cateogry_set.all()
		return {'bakery_items': bakery_categories}


def handicraft_items(request):
		handicraft_categories = Cateogry.objects.get(name="Handicrafts")
		handicraft_categories = handicraft_categories.cateogry_set.all()
		return {'handicraft_items': handicraft_categories}


def all_unique_products(request):
		return {'all_unique_products': Product.objects.filter(parent_product__isnull=True)}
