from django.shortcuts import render
from django.core.paginator import Paginator

from apps.products import models
from apps.cms.models import Slider

# ecommerce
def products(request):
    title = 'Продукты'
    big_categories = models.BigCategory.objects.prefetch_related('categories').all()
    categories = models.Category.objects.all()
    slider = Slider.objects.all()
    # new_products_indices = [products.id for products in models.Products.objects.all().order_by('-id')[:3]]
    category_id = request.GET.get('category_id')
    filter_type = request.GET.get('filter')

    if category_id:
        products = models.Products.objects.filter(category_id=category_id)
    else:
        products = models.Products.objects.all()

    if filter_type == 'newest':
        products = products.filter(is_new=True)
    
    elif filter_type == 'discount':
        products = products.filter(discount__gt=0) 

    paginator = Paginator(products, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
