from django.shortcuts import render
from testimonials.models import Testimonial_
from testimonials.forms import TestimonialForm

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


