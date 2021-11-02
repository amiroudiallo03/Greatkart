from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')


def dashboard(request):

    return render(request, 'dashboard.html')


def product_detail(request):

    return render(request, 'product-detail.html')


def register(request):

    return render(request, 'register.html')

def signin(request):

    return render(request, 'signin.html')

def store(request):
    
    return render(request, 'store.html')


def cart(request):

    return render(request, 'cart.html')

def order_complete(request):

    return render(request, 'order_complete.html')


def place_order(request):

    return render(request, 'place-order.html')