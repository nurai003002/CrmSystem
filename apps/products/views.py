from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from apps.products import models
from apps.cms.models import Slider, Services
from apps.cart.models import CartItem
from apps.billings.models import Billing, BillingProduct

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

    paginator = Paginator(products, 1)  
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
    title = "Биллинги"
    delivery_cost = 250
    billings = Billing.objects.all()
    cart_items = CartItem.objects.all()
    for billing in billings:
        billing.formatted_id = f"#SK{billing.id}"
    total_price = sum(item['total'] if isinstance(item, dict) else item.total for item in cart_items)
    if total_price < 15000:
        total_price += delivery_cost
    else:
        free_delivery = True
    
    paginator = Paginator(billings, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    
    return render(request, 'applications/products/orders.html', locals())

@require_POST
def delete_cart_item(request, cart_item_id):
    if request.user.is_authenticated: 
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        
        try:
            cart_item.delete() 
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'User not authenticated'})

@require_POST
def delete_billing(request, billing_id):
    print("Запрос на удаление получен для ID:", billing_id)  

    billing = get_object_or_404(Billing, id=billing_id)
    billing.delete()
    print("Биллинг удален:", billing_id)  
    return JsonResponse({"success": True})

def checkout(request):
    title = "Заказать"
    delivery_cost = 250
    cart_items = CartItem.objects.all()
    
    for item in cart_items:
        item.item_price = item.product.price * item.quantity
    total_price_first = sum(item['total'] if isinstance(item, dict) else item.total for item in cart_items)
    total_price = sum(item.item_price for item in cart_items)  
    if total_price < 15000:
        total_price += delivery_cost
    else:
        free_delivery = True

    if request.method == "POST":
        if 'checkout_oparation' in request.POST:
            data = {
                'first_name': request.POST.get('first_name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),  
                'region': request.POST.get('region'),
                'street': request.POST.get('street'),
                'apartment': request.POST.get('apartment'),
                'country': request.POST.get('country'),
                'city': request.POST.get('city'), 
                'zip_code': request.POST.get('zip_code'),
            }
            
            product = Billing(**data)
            product.save()
            
            cart_items.delete()  
            
            return redirect('orders')
    return render(request, 'applications/products/checkout.html', locals())

def customers(request):
    return render(request, 'applications/products/customers.html', locals())

def add_product(request):
    title = "Добавить товар"
    categories = models.Category.objects.all()
    products = models.Products.objects.all()
    color = models.Products.objects.values_list('color', flat=True).distinct() 
    status = models.Products.objects.values_list('status', flat=True).distinct() 

    if request.method == "POST" :
        if 'add_products' in request.POST:
            data = {
                'title': request.POST.get('title'),
                'category': models.Category.objects.get(id=request.POST.get('choices_category')) if request.POST.get('choices_category') else None,
                'description': request.POST.get('description'),
                'color': request.POST.get('color'),  
                'status': request.POST.get('status'),
                'is_new': request.POST.get('is_new') == 'on',
                'brand': request.POST.get('brand'), 
                'image': request.FILES.get('image'),
                'material': request.POST.get('material'),
                'cost_price': request.POST.get('cost_price'),
                'price': request.POST.get('price'),
                'old_price': request.POST.get('old_price'),
                'quantity': request.POST.get('quantity'),
                'manufacturer': request.POST.get('manufacturer'),
                'discount': request.POST.get('discount') or None
            }
            
            product = models.Products(**data)
            product.save()
            return redirect('products_list')
    
        if 'add_image' in request.POST:
            data = {
            'product': models.Products.objects.get(id=request.POST.get('choices_product')) if request.POST.get('choices_product') else None,
            'image': request.FILES.get('image')}

            products = models.ProductImage(**data)
            products.save()

            return redirect('products_list')
        
        if 'add_feature' in request.POST:
            data = {
            'product': models.Products.objects.get(id=request.POST.get('choices_product')) if request.POST.get('choices_product') else None,
            'feature': request.POST.get('feature')}

            products = models.ProductsFeature(**data)
            products.save()

            return redirect('products_list')
            
    return render(request, 'applications/products/add-product.html', 
                  {'title': title,
                    'categories': categories,
                    'products': products,
                    'color_choices': models.Products.COLOR_CHOICES,
                    'status_choices': models.Products.STATUS_CHOICES,})

def add_category(request):
    title = 'Категории'
    categories = models.Category.objects.all()
    big_categories = models.BigCategory.objects.all()
    if request.method == "POST" :
        if 'add_big_catergory' in request.POST:
            data = {
                'title': request.POST.get('title'),
            }
            
            big_category = models.BigCategory(**data)
            big_category.save()
            return redirect('add_product')

        if 'add_catergory' in request.POST:
            data = {
                'big_category': models.BigCategory.objects.get(id=request.POST.get('choices_big_category')) if request.POST.get('choices_big_category') else None,
                'title': request.POST.get('title'),
            }
            
            category = models.Category(**data)
            category.save()
            return redirect('add_product')
        
    return render(request, 'applications/products/category.html',
                  {'title': title,
                    'categories': categories,
                    'big_categories': big_categories,})

@require_POST
def delete_product(request, product_id):
    print("Запрос на удаление получен для ID:", product_id)  

    product = get_object_or_404(models.Products, id=product_id)
    product.delete()
    print("Товар удален:", product_id)  
    return JsonResponse({"success": True})

def products_list(request):
    title = "Список продуктов"
    product_list = models.Products.objects.all()
    for product in product_list:
        product.formatted_id = f"#SK{product.id}"
    return render(request, 'applications/products/products_list.html', locals())