from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, Category

def index(request):
    products = Product.objects.order_by('-list_date').filter(is_published=True)
    cat = Category.objects.all().filter(has_img=True)[:3]

    context = {
        'products' : products,
        'cat' : cat
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
