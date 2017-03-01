from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import is_safe_url
from django.views.decorators.http import require_POST
from shop.models import ModifiedProduct
from orders.models import Pincode
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


def check_availability(pincode, product_id):
    pincode_details = Pincode.objects.filter(pincode=pincode)
    availability = False
    if pincode_details:
        universal_availability = ModifiedProduct.objects.get(pk=product_id).productavailability.available_pincode.filter(pincode=999999)
        if universal_availability:
            return {'availability': True, 'pincode_details': pincode_details}
        else:
            availability = ModifiedProduct.objects.get(pk=product_id).productavailability.available_pincode.filter(pincode=pincode)
            if availability:
                availability = True
            else:
                availability = False
            return {'availability': availability, 'pincode_details': pincode_details}
    else:
        return {'availability': False, 'pincode_details': None}


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ModifiedProduct, id=product_id)
    form = CartAddProductForm(request.POST)
    availability = False
    prev = request.GET.get('prev', None)
    try:
        pincode = int(request.session['pincode'])
        print(request.session['pincode'])
        availability = check_availability(pincode, product_id)['availability']
        print(availability)
    except:
        pass
    if not availability:
        messages.success(request, "Product is not available at your Pincode\
                         or you haven't provided the pincode yet.")
        return redirect(prev)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ModifiedProduct, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                       initial={'quantity': item['quantity'],
                                                'update':True}
                                       )
    return render(request, 'cart/detail.html', {'cart': cart})
