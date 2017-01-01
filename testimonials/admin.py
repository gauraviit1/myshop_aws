from django.contrib import admin
from .models import Testimonial_

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment']
    list_filter = ['name']
    
admin.site.register(Testimonial_,TestimonialAdmin)
