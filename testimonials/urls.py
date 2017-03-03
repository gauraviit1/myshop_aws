from django.conf.urls import url
from testimonials import views


urlpatterns = [
    url(r'^$', views.read_and_write_testimonial, name='testimonial_list'),
    url(r'^selected-testimonials/$', views.selected_testimonials,
        name='selected_testimonials'),
]
