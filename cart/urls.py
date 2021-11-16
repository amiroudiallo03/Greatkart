from django.urls import path
from cart.views import *



urlpatterns = [
    path('cart/', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('increment_quantity/<int:product_id>/', increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<int:product_id>/', decrement_quantity, name='decrement_quantity'),
    path('remove_to_cart/<int:product_id>/', remove_to_cart, name='remove_to_cart'),
    
    
]