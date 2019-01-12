from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):

    # latest first
    # products = Product.objects.order_by('-list_date').filter(is_published=True)
    products = Product.objects.all().filter(is_published=True)
    count = len(products)   #number of products fetched

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products' : paged_products,
        'len' : count,
    }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product
    }
    return render(request, 'products/product.html', context)

def search(request):
    queryset_list = Product.objects.order_by('-list_date')

    #taking keywords from request
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(tags__icontains=keywords)

    count = len(queryset_list)
    context = {
        'products' : queryset_list,
        'len' : count
    }
    return render(request, 'products/search.html', context)