from django.shortcuts import render

from apps.products import models
from apps.cart.models import CartItem
# Create your views here.

def cart(request):
    title = "Корзина"
    cart_items = CartItem.objects.all()
    # products_detail = get_object_or_404(models.Products )
    return render(request, 'applications/products/cart.html', locals())