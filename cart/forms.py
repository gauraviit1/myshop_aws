from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # def __init__(self, *args, **kwargs):
        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     Fieldset(
        #     ),
        #     ButtonHolder(
        #         Submit('submit', 'Submit', css_class='button white')
        #     )
        # )
        # super(ExampleForm, self).__init__(*args, **kwargs)
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
