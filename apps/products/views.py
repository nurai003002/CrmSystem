from django.shortcuts import render

from apps.products import models
from apps.cms.models import Slider
# Create your views here.

# ecommerce
def products(request):
    product = models.Products.objects.all()
    big_categories = models.BigCategory.objects.all()
    categories = models.Category.objects.all()
    slider = Slider.objects.all()
    title = 'Продукты'  
    return render(request, 'applications/products/products.html', locals())

def product_detail(request):
    return render(request, 'applications/products/detail.html', locals())

def orders(request):
    return render(request, 'applications/products/orders.html', locals())

def checkout(request):
    return render(request, 'applications/products/checkout.html', locals())

def customers(request):
    return render(request, 'applications/products/customers.html', locals())

def cart(request):
    return render(request, 'applications/products/cart.html', locals())

def checkout(request):
    return render(request, 'applications/products/checkout.html', locals())

def shops(request):
    return render(request, 'applications/products/shops.html', locals())

def add_product(request):
    return render(request, 'applications/products/add-product.html', locals())
