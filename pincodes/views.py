from django.shortcuts import render


# Create your views here.

def check_availability(request, pincode, product_id):
    product = ModifiedProduct.objects.get(pk=product_id).productavailability.available_pincode.all()
    if pincode in
