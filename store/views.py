from django.shortcuts import render, get_object_or_404
from . import models
from store.models import Category
# Create your views here.


def index(request):
    products = models.Product.objects.filter(is_availaible=True).all()[:8]

    return render(request, 'index.html', locals())


def store(request, category_slug=None):
    categories = None
    product = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = models.Product.objects.filter(category=categories, is_availaible=True)
        product_count = products.count()
    else:
        products = models.Product.objects.filter(is_availaible=True).all()
        product_count = products.count()
    
    return render(request, 'store.html', locals())


def product_detail(request, slug):
    try:
        product = get_object_or_404(models.Product, slug=slug)
    except Exception as e:
        raise e
    return render(request, 'product-detail.html', locals())

def dashboard(request):

    return render(request, 'dashboard.html')




def register(request):

    return render(request, 'register.html')

def signin(request):

    return render(request, 'signin.html')



def cart(request):

    return render(request, 'cart.html')

def order_complete(request):

    return render(request, 'order_complete.html')


def place_order(request):

    return render(request, 'place-order.html')