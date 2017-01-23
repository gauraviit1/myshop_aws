from django.contrib import admin
from storemaps.models import Maps
# Register your models here.


class MapsAdmin(admin.ModelAdmin):
		list_display = ['url', 'jail']


admin.site.register(Maps, MapsAdmin)