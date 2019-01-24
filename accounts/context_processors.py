from .models import Cart, User  
from products.models import Category

def cart_processor(request):

    active = request.user.id

    categories = Category.objects.order_by('category')

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
            'categories': categories,
        }
        return context

    context = {
        'categories': categories
    }
    return context
 
    
