from django import forms

from django.utils.safestring import mark_safe

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int, label=mark_safe("<small>Quantity</small>"))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
