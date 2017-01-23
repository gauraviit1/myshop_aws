from django.shortcuts import render
from storemaps.models import Maps

# Create your views here.


def show_map(request):
		maps_url = Maps.objects.all()
		return render(request, 'storemaps/maps.html', {'maps_url': maps_url, })
