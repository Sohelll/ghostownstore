from .models import Cart, User  
from products.views import active_user_ajax
from accounts.views import active_user

def cart_processor(request):
    
    act_user_ac = active_user()
    act_user_pr = active_user_ajax()

    if(act_user_ac != 0):

        cart_item = Cart.objects.filter(user_id=act_user_ac)
        count = cart_item.count()

        print('-'*50)
        print(count)
        print('ac gave this {}'.format(act_user_ac))
        print(cart_item)
        print('-'*50)

        context = {
            'cart_item': cart_item,
            'len_cart': count,
        }
        return context
    
    elif(act_user_ac == -17):
        cart_item = Cart.objects.filter(user_id=act_user_ac)
        count = cart_item.count()

        print('-'*50)
        print(count)
        print('ac logout gave this {}'.format(act_user_ac))
        print(cart_item)
        print('-'*50)

        context = {
            'cart_item': cart_item,
            'len_cart': count,
        }
        return context
    else:
        cart_item = Cart.objects.filter(user_id=act_user_pr)
        count = cart_item.count()

        print('-'*50)
        print(count)
        print('pr gave this {}'.format(act_user_pr))
        print(cart_item)
        print('-'*50)

        context = {
            'cart_item': cart_item,
            'len_cart': count,
        }
        return context


    
