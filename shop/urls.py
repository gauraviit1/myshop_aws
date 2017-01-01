from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.mainPage, name='main_page'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<cateogry_slug>[-\w]+)/$', views.product_list,
        name='product_list_by_cateogry'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]
