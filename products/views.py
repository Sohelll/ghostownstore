from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, HttpResponse
from accounts.models import User, Cart
from django.core import serializers

def index(request):

    # latest first
    # products = Product.objects.order_by('-list_date').filter(is_published=True)
    products = Product.objects.all().filter(is_published=True)  #take all of them for now!
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
        'len' : count,
        'prev_search' : request.GET['keywords']
    }
    return render(request, 'products/search.html', context)


def cat_wise(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)

    products = Product.objects.order_by('-list_date').filter(category=category_id)
    count = len(products)

    print('-'*30)
    print(products)
    print('-'*30)

    context = {
        'cat' : cat,
        'products' : products,
        'len' : count
    }
    return render(request, 'products/cat_wise.html', context)

def add_to_cart(request):
    p_id = request.GET['product_id']
    u_id = request.GET['userid']
    active_user_id = u_id
    print(p_id)
    print(u_id)

    item_exists = Cart.objects.filter(user_id=u_id, cart_product_id=p_id).exists()
    if item_exists:
        users_cart = Cart.objects.filter(user_id=u_id)
        print('-'*30)
        print(users_cart)
        print('-'*30)

        response = serializers.serialize("json", users_cart)
        print(response)
        return HttpResponse(response, content_type='application/json')    
    else:
        user_instance = User(id=u_id)       #Adding instances to cart fields
        product_instance = Product(id=p_id) #same here
        car_t = Cart(user=user_instance, cart_product=product_instance)     #saving as cart item

        car_t.save()

        users_cart = Cart.objects.filter(user_id=u_id)      #fetching current user's cart
        data = {
            'users_cart': str(users_cart)
        }

        return JsonResponse(data, safe=False)

