from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, HttpResponse
from accounts.models import User, Cart, UserProfileInfo
from django.core import serializers
from django.contrib import messages

active_pr = 0

def index(request):

    # latest first
    # products = Product.objects.order_by('-list_date').filter(is_published=True)
    products = Product.objects.order_by('list_date').filter(is_published=True)  #take all of them for now!
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
    count = products.count()

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

    global active_pr
    active_pr = u_id

    item_exists = Cart.objects.filter(user_id=u_id, cart_product_id=p_id).exists()
    if item_exists:
        users_cart = Cart.objects.filter(user_id=u_id)
        products_in_cart = users_cart.count()

        data = {
            'msg': 'Already in the cart',
            'change' : False,
            'products_in_cart' : products_in_cart,
        }
        return JsonResponse(data)    
    else:
        user_instance = User(id=u_id)       #Adding instances to cart fields
        product_instance = Product(id=p_id) #same here
        car_t = Cart(user=user_instance, cart_product=product_instance)     #saving as cart item

        car_t.save()

        users_cart = Cart.objects.filter(user_id=u_id)
        products_in_cart = users_cart.count()

        data = {
            'msg': 'item added to cart',
            'products_in_cart': products_in_cart,
            'change': True,
        }

        return JsonResponse(data)


def delete_from_cart(request):
    p_id = request.GET['product_id']
    u_id = request.GET['userid']

    global active_pr
    active_pr = u_id

    item_exists = Cart.objects.filter(
        user_id=u_id, cart_product_id=p_id).exists()
    if item_exists:
        del_item = Cart.objects.filter(
            user_id=u_id, cart_product_id=p_id)

        del_item.delete()

        users_cart = Cart.objects.filter(user_id=u_id)
        products_in_cart = users_cart.count()

        data = {
            'msg': 'item deleted from cart',
            'products_in_cart': products_in_cart,
            'change': True,
        }
        return JsonResponse(data)
    else:

        data = {
            'msg': 'item already deleted',
            'change': False,
        }

        return JsonResponse(data)


def checkout(request, user_id):

    user_products = Cart.objects.filter(user_id=user_id)
    user_det = UserProfileInfo.objects.filter(user=user_id)[0]

    subtotal = 0
    delivery = 0

    for p in user_products:
        subtotal += p.cart_product.actual_price       
        delivery += p.cart_product.delivery_charge

    total = subtotal + delivery

    context = {
        'user_products': user_products,
        'user_det': user_det,
        'subtotal': subtotal,
        'delivery': delivery,
        'total' : total
    }    

    return render(request, 'products/checkout.html', context)



def checkout_single(request, product_id):
    return render(request, 'products/checkout.html')

def checkout_tologin(request):
    messages.success(request, 'Please login first')
    return redirect('login')

def active_user_ajax():
    global active_pr
    return active_pr

