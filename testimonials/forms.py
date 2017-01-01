from django import forms
from testimonials.models import Testimonial_


class TestimonialForm(forms.ModelForm):
	class Meta:
		model = Testimonial_
		fields = ['name', 'comment',]
