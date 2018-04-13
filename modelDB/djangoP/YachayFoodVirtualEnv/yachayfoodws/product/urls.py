from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^product/$', views.product_list),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail),
]
