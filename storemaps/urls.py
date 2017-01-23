from django.conf.urls import url
from storemaps import views

urlpatterns = [
    url(r'^$', views.show_map, name='show_map'),
]
