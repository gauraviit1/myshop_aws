from django.conf.urls import url
from pincodes import views


urlpatterns = [
     url(
            r'^pincode-autocomplete/$',
            views.PincodeAutocomplete.as_view(),
            name='pincodes-autocomplete',
        ),
]
