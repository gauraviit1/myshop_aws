from django.contrib import admin
from shop.models import Cateogry, Product, ModifiedCategory, ModifiedProduct
from mptt.admin import MPTTModelAdmin


# Register your models here.\
class CateogryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Cateogry, CateogryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated', 'features',
                    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Pahal administration'

admin.site.site_title = 'Pahal administration'

class ModifiedCategoryAdmin(MPTTModelAdmin):
		list_filter = ['name']
		prepopulated_fields = {"slug": ("name",)}
    # specify pixel amount for this ModelAdmin only:


admin.site.register(ModifiedCategory, ModifiedCategoryAdmin)

class ModifiedProductAdmin(MPTTModelAdmin):
		list_filter = ['name', 'price', 'category', 'parent']
		prepopulated_fields = {"slug": ("name",)}
    # specify pixel amount for this ModelAdmin only:


admin.site.register(ModifiedProduct, ModifiedProductAdmin)