from .models import Category
from cart.views import _cart_id, add_cart
from cart.models import Cart, CartItem

def menu_link(request):
    links = Category.objects.all()

    return dict(links=links)


def cart_count(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    cart_items_count = cart_items.count()

    return dict(cart_items_count=cart_items_count)