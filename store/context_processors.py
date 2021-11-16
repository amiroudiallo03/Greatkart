from .models import Category
from cart.views import _cart_id, add_cart
from cart.models import Cart, CartItem

def menu_link(request):
    links = Category.objects.all()

    return dict(links=links)


def cart_count(request, count=0):
    
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
    
    for cart_item in cart_items:
        
        count += cart_item.quantity

    
        
        
    return dict(count=count)