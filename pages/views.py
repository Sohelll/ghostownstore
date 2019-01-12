from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def index(request):
    products = Product.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'products' : products
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
