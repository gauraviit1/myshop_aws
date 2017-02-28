from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import is_safe_url
from django.views.decorators.http import require_POST
from shop.models import ModifiedProduct
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


def check_availability(request, pincode, product_id):
    availability = ModifiedProduct.objects.get(pk=product_id).productavailability.available_pincode.filter(pincode=pincode)
    if availability:
        return True
    else:
        return False

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ModifiedProduct, id=product_id)
    form = CartAddProductForm(request.POST)
    availability = False
    prev = request.GET.get('prev', None)
    if not is_safe_url(prev):
        prev = None
    try:
        pincode = int(request.session['pincode'])
        availability = check_availability(pincode, product_id)
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
