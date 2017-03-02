from django.contrib import admin
from pincodes.models import Pincode


# Register your models here.
@admin.register(Pincode)
class PincodeAdmin(admin.ModelAdmin):
    list_display = ['pincode', 'officeName', 'districtName', 'stateName']
    search_fields = ['pincode', 'officeName', 'districtName']
