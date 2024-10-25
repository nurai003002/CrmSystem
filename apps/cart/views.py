from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from apps.products import models
from apps.cart.models import CartItem
# Create your views here.

def cart(request):
    title = "Корзина"
    delivery_cost = 250
    free_delivery = False
    cart_items = []

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        session_cart = request.session.get('cart', [])
        for item in session_cart:
            product = get_object_or_404(models.Products, pk=item['product_id'])
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'total': item['total'],
            })

    cart_items_count = len(cart_items)
    total_price = sum(item['total'] if isinstance(item, dict) else item.total for item in cart_items)

    if total_price < 15000:
        total_price += delivery_cost
    else:
        free_delivery = True
    return render(request, 'applications/products/cart.html', locals())


def add_to_cart(request, product_id):
    product_item = get_object_or_404(models.Products, pk=product_id)
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product_item,
            defaults={'quantity': 0, 'total': 0}
        )
        cart_item.quantity += int(request.GET.get('quantity', 1))
        cart_item.total = cart_item.quantity * product_item.price
        cart_item.save()
    else:
        cart = request.session.get('cart', [])
        quantity_to_add = int(request.GET.get('quantity', 1))
        item_found = False

        for item in cart:
            if item['product_id'] == product_id:
                item['quantity'] += quantity_to_add
                item['total'] = item['price'] * item['quantity']
                item_found = True
                break

        if not item_found:
            cart.append({
                'product_id': product_id,
                'title': product_item.title,
                'price': product_item.price,
                'quantity': quantity_to_add,
                'total': product_item.price * quantity_to_add
            })

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')


# @require_POST
# def update_cart_quantity(request):
#     data = json.loads(request.body)
#     product_id = data.get('product_id')
#     quantity = data.get('quantity')

#     if product_id and quantity:
#         try:
#             cart_item = CartItem.objects.get(id=product_id)
#             cart_item.quantity = quantity
#             cart_item.save()

#             return JsonResponse({'success': True, 'price': cart_item.product.price})
#         except CartItem.DoesNotExist:
#             return JsonResponse({'success': False}, status=404)
#     return JsonResponse({'success': False}, status=400)