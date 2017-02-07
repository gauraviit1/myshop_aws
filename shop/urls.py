from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.mainPage, name='main_page'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^termsandconditions/$', views.termsandconditions, name='terms_and_conditions'),
    url(r'^privacypolicy/$', views.privacypolicy, name='privacy_policy'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]
