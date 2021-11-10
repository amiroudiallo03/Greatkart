from django.db import models

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, null=True)
    date_add = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = ("cart")
        verbose_name_plural = ("carts")



class CartItem(models.Model):
    product = models.ForeignKey("store.Product", related_name='product_cartitem', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    
        
    class Meta:
        verbose_name = ("cartitem")
        verbose_name_plural = ("cart_items")

    