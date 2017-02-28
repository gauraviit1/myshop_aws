from django.contrib import admin
from pincodes.models import Pincode


# Register your models here.
@admin.register(Pincode)
class PincodeAdmin(admin.ModelAdmin):
    pass
