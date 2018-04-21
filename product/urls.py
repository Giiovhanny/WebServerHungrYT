from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^product/$', views.product_list),
    url(r'^product/delete/(\d+)/$', views.delete),
]