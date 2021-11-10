from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_add')
    search_fields = ('cart_id',)
    

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_display_links = ('product', 'cart', 'quantity')
    search_fields = ('product', 'cart')