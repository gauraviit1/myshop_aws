from django.shortcuts import render
from dal import autocomplete
from pincodes.models import Pincode


# Create your views here.
def check_availability(request, pincode, product_id):
    product = ModifiedProduct.objects.get(pk=product_id).productavailability.available_pincode.all()
    pass

class PincodeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Pincode.objects.none()
        qs = Pincode.objects.all()
        if self.q:
            qs = qs.filter(pincode__istartswith=self.q)
        return qs
