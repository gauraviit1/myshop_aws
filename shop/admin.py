from django.contrib import admin
from shop.models import Cateogry, Product, Attribute


# Register your models here.\
class CateogryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Cateogry, CateogryAdmin)


class AttributeInLine(admin.TabularInline):
		model = Attribute


class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated',
                    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {"slug": ('name',)}
    inlines = [AttributeInLine]

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Pahal administration'

admin.site.site_title = 'Pahal administration'