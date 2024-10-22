from django.shortcuts import render
from django.shortcuts import get_object_or_404

from apps.products import models
# Create your views here.

def cart(request):
    title = "Корзина"
    # products_detail = get_object_or_404(models.Products )
    return render(request, 'applications/products/cart.html', locals())
