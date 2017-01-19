from django.shortcuts import render, get_object_or_404
from shop.models import Cateogry, Product, Attribute
from cart.forms import CartAddProductForm
from testimonials.models import Testimonial_


# Create your views here.
def product_list(request, cateogry_slug=None):
    cateogry = None
    cateogries = Cateogry.objects.all()
    testimonials = Testimonial_.objects.all()[:5]
    products = Product.objects.filter(available=True)
    if cateogry_slug:
        cateogry = get_object_or_404(Cateogry,slug=cateogry_slug)
        products = products.filter(cateogry=cateogry)
    return render(request, 'shop/product/list.html', {
        'cateogry': cateogry,
        'cateogries': cateogries,
        'products': products,
        'testimonials':testimonials,
    })


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id,
                                     slug=slug,
                                     available=True)

    options = [v for v in product.features['Variety'].values()]
    options_attribute = ''
    for key in options[0]:
        print(key)
        options_attribute = key
    print(options_attribute)   
    price_list = [v['price'] for v in options]
    options_list = [v[options_attribute] for v in options]
    
    zipped_price_option = zip(price_list, options_list)
    print(zipped_price_option)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'zipped_price_option': zipped_price_option,
                   })


def mainPage(request):
    cateogries = Cateogry.objects.all()
    first_testimonial = Testimonial_.objects.first()
    testimonials = Testimonial_.objects.all()[:5]
    return render(request, 'shop/product/main.html', {'cateogries': cateogries, 
                                                       'testimonials': testimonials,
                                                       'first_testimonial': first_testimonial,} )


