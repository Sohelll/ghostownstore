from .models import Cart, User  

def cart_processor(request):

    active = request.user.id

    if active is not None:

        cart_item = Cart.objects.filter(user_id=active)
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

    context = {}
    return context
 
    
