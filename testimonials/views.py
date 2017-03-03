from django.shortcuts import render
from testimonials.models import Testimonial_
from testimonials.forms import TestimonialForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json


def read_and_write_testimonial(request):
    testimonials = Testimonial_.objects.all()
    if request.method == 'POST':
    	form = TestimonialForm(request.POST)
    	if form.is_valid():
    		form.save()
    else:
    	form = TestimonialForm()
    return render(request, 'testimonial/testimonial.html',
                  {'form': form,
                   'testimonials': testimonials})


def selected_testimonials(request):
    testimonials = Testimonial_.objects.all().values('name', 'comment')[:5]
    # data = serializers.serialize("json", testimonials)
    data = json.dumps(list(testimonials))
    return HttpResponse(data, content_type='application/json')
