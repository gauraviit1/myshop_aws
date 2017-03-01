from django.contrib import admin
from shop.models import Cateogry, Product, ModifiedCategory, ModifiedProduct, ProductImages
from django_mptt_admin.admin import DjangoMpttAdmin
from orders.forms import ProductAvailabilityForm
from orders.models import ProductAvailability


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


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
    fields = ['image', 'image_tag']
    readonly_fields = ('image_tag',)


class ProductAvailabilityAdminInline(admin.StackedInline):
    model = ProductAvailability
    form = ProductAvailabilityForm


class ModifiedProductAdmin(DjangoMpttAdmin):
    tree_auto_open = 3
    list_display = ['name', 'price', 'option_type', 'is_unique']
    list_editable = ['price', 'option_type', 'is_unique']
    list_filter = ['name', 'price', 'category', 'parent']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductAvailabilityAdminInline, ProductImagesAdmin, ]


admin.site.register(ModifiedProduct, ModifiedProductAdmin)
