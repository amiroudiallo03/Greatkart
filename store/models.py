from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.


class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        abstract=True

  
class Category(Base):
    category_name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='category_name')
    picture = models.FileField(upload_to="picture_categorie")
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):

        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
    
class Product(Base):
    product_name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from= 'product_name')
    images = models.FileField(upload_to='images_product')
    price = models.FloatField()
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    is_availaible = models.BooleanField(default=True)
    category = models.ForeignKey("Category", related_name='category_product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name
    
    def get_url(self):

        return reverse('product-detail', args=[self.slug])