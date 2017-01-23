from django.contrib import admin
from storemaps.models import Maps
# Register your models here.


class MapsAdmin(admin.ModelAdmin):
		list_display = ['name', 'controller_jail', 'url', ]


admin.site.register(Maps, MapsAdmin)
