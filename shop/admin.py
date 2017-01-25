from django.contrib import admin
from shop.models import Cateogry, Product, ModifiedCategory, ModifiedProduct
from django_mptt_admin.admin import DjangoMpttAdmin


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

class ModifiedCategoryAdmin(DjangoMpttAdmin):
    tree_auto_open = 3
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(ModifiedCategory, ModifiedCategoryAdmin)

class ModifiedProductAdmin(DjangoMpttAdmin):
    tree_auto_open = 3
    list_filter = ['name', 'price', 'category', 'parent']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ModifiedProduct, ModifiedProductAdmin)