from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Cateogry, Product
from cart.forms import CartAddProductForm
from testimonials.models import Testimonial_


# Create your views here.
def mainPage(request):
    cateogries = Cateogry.objects.all()
    first_testimonial = Testimonial_.objects.first()
    testimonials = Testimonial_.objects.all()[:5]
    return render(request, 'shop/product/main.html', {'cateogries': cateogries,
                                                      'testimonials': testimonials,
                                                      'first_testimonial': first_testimonial, })


def product_list(request, cateogry_slug=None):
    cateogry = None
    cateogries = Cateogry.objects.all()
    testimonials = Testimonial_.objects.all()[:5]
    products = Product.objects.filter(available=True)
    if cateogry_slug:
        cateogry = get_object_or_404(Cateogry, slug=cateogry_slug)
        products = products.filter(cateogry=cateogry)
    return render(request, 'shop/product/list.html', {
        'cateogry': cateogry,
        'cateogries': cateogries,
        'products': products,
        'testimonials': testimonials,
    })


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True)
    child_products = product.product_set.all()

    if child_products:
        return redirect(child_products[0])

    else:
        try:
            child_products = product.parent_product.product_set.all()
        except:
            child_products = {}

    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'child_products': child_products,
                   })
