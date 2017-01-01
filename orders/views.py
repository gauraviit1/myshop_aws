from django.shortcuts import render
from django.core.mail import send_mail
from orders.models import OrderItem, Order
from orders.forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            order_created(order.id)
            return render(request,'orders/order/created.html',{
                'order': order
            })
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart':cart, 'form':form})

def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr.'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your' \
              ' order id is {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
