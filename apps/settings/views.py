from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html', locals())


def sales(request):
    return render(request, 'dashboard/sales.html', locals())


def calendar(request):
    return render(request, 'applications/apps-calendar.html', locals())

def todo(request):
    return render(request, 'applications/apps-todo.html', locals())


def manager(request):
    return render(request, 'applications/apps-file-manager.html', locals())

def chat(request):
    return render(request, 'applications/apps-chat.html', locals())

def products(request):
    return render(request, 'ecommerce/products.html', locals())

def product_detail(request):
    return render(request, 'ecommerce/product-detail.html', locals())

def orders(request):
    return render(request, 'ecommerce/orders.html', locals())

def checkout(request):
    return render(request, 'ecommerce/checkout.html', locals())

def customers(request):
    return render(request, 'ecommerce/customers.html', locals())

def cart(request):
    return render(request, 'ecommerce/cart.html', locals())

def checkout(request):
    return render(request, 'ecommerce/checkout.html', locals())

def shops(request):
    return render(request, 'ecommerce/shops.html', locals())

def add_product(request):
    return render(request, 'ecommerce/add-product.html', locals())
