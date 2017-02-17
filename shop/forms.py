from django import forms

class PincodeForm(forms.Form):
    pincode = forms.IntegerField(label='Your Pincode', min_value=0)