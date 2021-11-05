from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Category)
class CategoriyAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'picture', 'description')
    search_field = ('category_name',)
    date_hierarchy = 'date_add'

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'image_view', 'description', 'price', 'category', 'status')
    search_field = ('product_name',)
    date_hierarchy = 'date_add'

    def image_view(self, obj):

        return mark_safe(f'<img src="{obj.images.url}" style="width:100px; height:100px">')