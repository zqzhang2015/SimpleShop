from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact_view(request):
    return render(request, 'contact.html')


def client_list_view(request):
    return render(request, 'clientList.html')


def product_list_view(request):
    return render(request, 'productList.html')


def client_detail_view(request):
    return render(request, 'clientDetail.html')


def product_detail_view(request):
    return render(request, 'productDetail.html')


def error_404(request):
    context = {}
    return render(request, 'error_404.html', context)