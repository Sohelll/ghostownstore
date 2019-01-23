from .models import Cart, User  
from products.views import active_user_ajax
from accounts.views import active_user

def cart_processor(request):

    #getting the user who is online    
    act_user_ac = active_user()
    act_user_pr = active_user_ajax()

    if(act_user_ac != 0):

        cart_item = Cart.objects.filter(user_id=act_user_ac)
        count = cart_item.count()

        subtotal = 0
        delivery = 0

        for c in cart_item:
            subtotal += c.cart_product.actual_price
            delivery += c.cart_product.delivery_charge

        total = subtotal + delivery 

        context = {
            'cart_item': cart_item,
            'len_cart': count,
            'subtotal': subtotal,
            'delivery': delivery,
            'total': total,
        }
        return context
    
    elif(act_user_ac == -17):
        cart_item = Cart.objects.filter(user_id=act_user_ac)
        count = cart_item.count()

        context = {
            'cart_item': cart_item,
            'len_cart': count,
        }
        return context
    else:
        cart_item = Cart.objects.filter(user_id=act_user_pr)
        count = cart_item.count()

        subtotal = 0
        delivery = 0

        for c in cart_item:
            subtotal += c.cart_product.actual_price
            delivery += c.cart_product.delivery_charge

        total = subtotal + delivery

        context = {
            'cart_item': cart_item,
            'len_cart': count,
            'subtotal': subtotal,
            'delivery': delivery,
            'total': total,
        }
        return context


    
