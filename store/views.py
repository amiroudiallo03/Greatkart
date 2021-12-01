from django.shortcuts import render, get_object_or_404
from . import models
from store.models import Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    products = models.Product.objects.filter(is_availaible=True).all()[:8]

    return render(request, 'index.html', locals())


def store(request, category_slug=None,):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = models.Product.objects.filter(category=categories, is_availaible=True).order_by('id')
        paginator = Paginator(products, 3)
        product_count = products.count()
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        #product_count = products.count()
    else:
        products = models.Product.objects.filter(is_availaible=True).all().order_by('id')
        paginator = Paginator(products, 6)
        product_count = products.count()
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

    return render(request, 'store.html', {'products': page_obj, 'product_count':product_count})


def product_detail(request, slug):
    try:
        product = get_object_or_404(models.Product, slug=slug)
    except Exception as e:
        raise e
    colors = models.Variation.objects.color()
    sizes = models.Variation.objects.size()
    return render(request, 'product-detail.html', locals())

    
@login_required
def dashboard(request):

    return render(request, 'dashboard.html')










# def cart(request):

#     return render(request, 'cart.html')

def order_complete(request):

    return render(request, 'order_complete.html')


def place_order(request):

    return render(request, 'place-order.html')


def search(request):
    search = request.GET['search']
    if search:
        products = models.Product.objects.filter(Q(product_name__icontains=search) | Q(description__icontains=search))
        product_count = products.count()
    return render(request, 'store.html', locals())


