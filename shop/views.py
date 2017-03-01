from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.db.models import Q
import operator
from functools import reduce
from shop.models import ModifiedCategory, ModifiedProduct
from cart.forms import CartAddProductForm
from testimonials.models import Testimonial_
import requests
import json
from shop.forms import PincodeForm
from cart.views import check_availability

from django.http import JsonResponse


# Create your views here.
def mainPage(request):
    first_testimonial = Testimonial_.objects.first()
    testimonials = Testimonial_.objects.all()
    return render(request, 'shop/product/main.html',
                  {'testimonials': testimonials,
                   'first_testimonial': first_testimonial, })


def product_list(request, category_slug=None):
    category = None
    products = ModifiedProduct.objects.filter(level=0)
    if category_slug:
        category = get_object_or_404(ModifiedCategory, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'products': products,
    })


def category_list(request, category_slug=None):
    category = get_object_or_404(ModifiedCategory, slug=category_slug).get_leafnodes()
    if not category:
        category = get_list_or_404(ModifiedCategory, slug=category_slug)
    else:
        category = get_object_or_404(ModifiedCategory, slug=category_slug).get_leafnodes()

    products = ModifiedProduct.objects.filter(category__in=category).filter(is_unique=True)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'products': products,
    })


def product_detail(request, id, slug):
    pincode_form = PincodeForm()
    product = get_object_or_404(ModifiedProduct, id=id,
                                slug=slug,
                                available=True)
    if product.is_root_node():
        child_products = product.get_children()
    else:
        child_products = product.parent.get_children()
    if product.get_children():
        return redirect(product.get_children()[0])
    else:
        cart_product_form = CartAddProductForm()

        if request.is_ajax():
            template = 'partial-results.html'
        else:
            template = 'shop/product/detail.html'
        return render(request, template,
                      {'product': product,
                       'cart_product_form': cart_product_form,
                       'child_products': child_products,
                       'pincode_form':pincode_form,
                       })

def termsandconditions(request):
    return render(request, 'shop/static_templates/termsandconditions.html')

def privacypolicy(request):
    return render(request, 'shop/static_templates/privacypolicy.html')


def pincode_availaiblity(request, id):
    pincode = request.GET.get('pincode', None)
    availability_details = check_availability(int(pincode), int(id))

    if availability_details['pincode_details']:
        is_valid_Pincode = True
        office = availability_details['pincode_details'][0].officeName
        district = availability_details['pincode_details'][0].districtName
        if availability_details['availability']:
            is_available = True
        else:
            is_available = False
    else:
        office = None
        district = None
        is_valid_Pincode = False
        is_available = False
    data = {
            'is_valid_Pincode': is_valid_Pincode,
            'is_available': is_available,
            'office': office,
            'district': district,
    }
    #
    # # address = "https://pincode.saratchandra.in/api/pincode/" + str(pincode)
    request.session['pincode'] = str(pincode)
    # response = requests.get(address)
    # json_data = json.loads(response.text)
    return JsonResponse(data)


def search(request):
    query_string = ''
    found_entries = None

    if (request.GET.get('q')) and request.GET.get('q').strip():
        values = request.GET.get('q').split()
        query_string = request.GET.get('q')
        products = ModifiedProduct.objects.filter(reduce(operator.or_,(Q(name__icontains=x) for
        x in values))).filter(is_unique=True)
        return render(request, 'shop/product/list.html',{'products': products, 'query_string':query_string})

    else:
        products = ModifiedProduct.objects.all().filter(is_unique=True)
        return render(request, 'shop/product/list.html',{'products': products})
