from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):

    # latest first
    # products = Product.objects.order_by('-list_date').filter(is_published=True)
    products = Product.objects.all().filter(is_published=True)

    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products' : paged_products
    }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    return render(request, 'products/product.html')
