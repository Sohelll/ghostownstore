from .models import Cart, User
from accounts.views import active_user

def cart_processor(request):
    print('-'*40)
    print(active_user())
    print('-'*40)
    
    cart_item = Cart.objects.filter(user_id=active_user())

    context = {
        'cart_item': cart_item
    }
    return context
