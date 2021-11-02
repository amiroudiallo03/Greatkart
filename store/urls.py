
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('order_complete', views.order_complete, name='order_complete'),
    path('place_order/', views.place_order, name='place_order'),
]
