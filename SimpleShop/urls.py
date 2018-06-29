from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.client_list_view, name='client-list'),
    path('products', views.product_list_view, name='product-list'),
    path('clients/<pk>', views.client_detail_view, name='client-detail'),
    path('products/<pk>', views.product_detail_view, name='product-detail'),
]
