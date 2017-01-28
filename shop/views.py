from django.shortcuts import render, get_object_or_404, redirect
from shop.models import ModifiedCategory, ModifiedProduct
from cart.forms import CartAddProductForm
from testimonials.models import Testimonial_


# Create your views here.
def mainPage(request):

    first_testimonial = Testimonial_.objects.first()
    testimonials = Testimonial_.objects.all()
    return render(request, 'shop/product/main.html', {
                                                      'testimonials': testimonials,
                                                      'first_testimonial': first_testimonial, })


def product_list(request, category_slug=None):
    category = None
    categories = ModifiedCategory.objects.all()
    testimonials = Testimonial_.objects.all()[:5]
    products = ModifiedProduct.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(ModifiedCategory, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'testimonials': testimonials,
    })


def product_detail(request, id, slug):

    product = get_object_or_404(ModifiedProduct, id=id,
                                slug=slug,
                                available=True)
    if product.is_root_node():
        child_products = product.get_children()
    else:
        child_products= product.parent.get_children()

    cart_product_form = CartAddProductForm()

    if request.is_ajax():
        template = 'partial-results.html'
    else:
        template = 'shop/product/detail.html'
    return render(request, template,
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'child_products': child_products,
                   })
