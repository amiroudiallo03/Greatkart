
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/<slug:category_slug>/', views.store, name='product_by_category'),
    #path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('store/product/<str:slug>/', views.product_detail, name='product-detail'),
    path('search/', views.search, name='search'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('store/', views.store, name='store'),
    path('order_complete', views.order_complete, name='order_complete'),
    path('place_order/', views.place_order, name='place_order'),
]
