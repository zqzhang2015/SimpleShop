from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Client, Product

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact_view(request):
    return render(request, 'contact.html')


def client_list_view(request):
    clients = Client.objects.all()
    return render(request, 'clientList.html', {'clients': clients})


def product_list_view(request):
    product_query = Product.objects.all()
    context = {
        'products': product_query
    }
    return render(request, 'productList.html', context)


def client_detail_view(request):
    return render(request, 'clientDetail.html')


def error_404(request):
    context = {}
    return render(request, 'error_404.html', context)


# CLIENT CRUD
class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client-list')


class ClientDetail(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client-list')


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')


# PRODUCT CRUD
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')