from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.mainPage, name='main_page'),
    url(r'^search/$', views.search, name="search"),
    url(r'^product/$', views.product_list, name='product_list'),
    url(r'^pincode/(?P<id>\d+)/', views.pincode_availaiblity, name='pincode_availaiblity'),
    url(r'^termsandconditions/$', views.termsandconditions, name='terms_and_conditions'),
    url(r'^privacypolicy/$', views.privacypolicy, name='privacy_policy'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]
