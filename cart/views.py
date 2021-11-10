from django.shortcuts import render, redirect
from .models import Cart, CartItem
from django.http import HttpResponse
from store.models import Product
from django.shortcuts import get_object_or_404
# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.create(cart_id=_cart_id(request))

    cart.save

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        quantity = 1
        cart_item.quantity = quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem(
            product=product,
            cart=cart,
            quantity = 1
        )
        cart_item.save()
    
    return redirect('cart')

def cart(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True).all()
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except Exception:
        pass
    return render(request, 'cart.html', locals())
    