from django import forms
from orders.models import Order
from dal import autocomplete
from orders.models import ProductAvailability

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


class ProductAvailabilityForm(forms.ModelForm):
    class Meta:
        model = ProductAvailability
        fields = ('product', 'available_pincode')
        widgets = {
            'available_pincode': autocomplete.ModelSelect2Multiple(
                'pincodes:pincodes-autocomplete'
            )
        }
