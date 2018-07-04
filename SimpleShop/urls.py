from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.client_list_view, name='client-list'),
    path('products', views.product_list_view, name='product-list'),
    path('contact', views.contact_view, name='contact'),
    path('orders', views.orders_view, name='order-list'),
    path('', include('django.contrib.auth.urls')),
]

handler404 = 'SimpleShop.views.error_404'

urlpatterns += [
    path('clients/create/', views.ClientCreate.as_view(), name='client-create'),
    path('clients/<int:pk>/update/', views.ClientUpdate.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', views.ClientDelete.as_view(), name='client-delete'),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name='client-detail'),
]

urlpatterns += [
    path('products/create/', views.ProductCreate.as_view(), name='product-create'),
    path('products/<slug:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('products/<slug:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('products/<slug:pk>', views.ProductDetail.as_view(), name='product-detail'),
]

urlpatterns += [
    path('orders/create/', views.create_order, name='order-create'),
    path('orders/<int:pk>/update/', views.edit_order, name='order-update'),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='order-delete'),
]