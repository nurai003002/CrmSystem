from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from apps.products import models
from apps.cms.models import Slider, Services

# ecommerce
def products(request):
    title = 'Продукты'
    big_categories = models.BigCategory.objects.prefetch_related('categories').all()
    categories = models.Category.objects.all()
    slider = Slider.objects.all()
    category_id = request.GET.get('category_id')
    filter_type = request.GET.get('filter')
    color_filter = request.GET.getlist('color')

    if category_id:
        products = models.Products.objects.filter(category_id=category_id)
    else:
        products = models.Products.objects.all()

    if filter_type == 'newest':
        products = products.filter(is_new=True)
    
    elif filter_type == 'discount':
        products = products.filter(discount__gt=0)

    if color_filter:
        products = products.filter(color__in=color_filter)

    paginator = Paginator(products, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    colors = models.Products.COLOR_CHOICES 

    return render(request, 'applications/products/products.html', locals())

def product_detail(request, id):
    title = 'Информация о товаре'
    products = models.Products.objects.all()
    products_detail = get_object_or_404(models.Products, id=id)
    service = Services.objects.latest('id')
    reviews = models.ProductReview.objects.filter(product=id).order_by('-created_at')
    review_amount = reviews.count()
    
    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            new_comment = models.ProductReview.objects.create(
                product=products_detail,
                text=text,
                user=request.user
            )
            new_comment.save()
            return redirect('product_detail', id=id)
        
    return render(request, 'applications/products/detail.html', locals())

def orders(request):
    return render(request, 'applications/products/orders.html', locals())

def checkout(request):
    return render(request, 'applications/products/checkout.html', locals())

def customers(request):
    return render(request, 'applications/products/customers.html', locals())

def checkout(request):
    return render(request, 'applications/products/checkout.html', locals())

def shops(request):
    return render(request, 'applications/products/shops.html', locals())

def add_product(request):
    return render(request, 'applications/products/add-product.html', locals())
