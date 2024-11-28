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
from apps.users.models import User
# Create your views here.

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
    
    billings = Billing.objects.all().order_by('-created') 
    paginator = Paginator(billings, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'applications/products/orders/orders.html', locals())

def orders_edit(request, order_id):
    title = "Редактировать биллинг"
    billings = get_object_or_404(Billing, id=order_id)
    users = User.objects.all()

    if request.method == "POST":
        if 'edit_order' in request.POST:
            billings.billing_type = request.POST.get('billing_type_choices')
            billings.billing_receipt_type = request.POST.get('billing_receipt_type_choices')
            billings.billing_payment_status = request.POST.get('billing_payment_status')
            billings.billing_status = request.POST.get('billing_status')
            billings.billing_payment = request.POST.get('billing_payment')
            billings.user = User.objects.get(id=request.POST.get('users'))
            billings.email = request.POST.get('email')
            billings.first_name = request.POST.get('first_name')
            billings.last_name = request.POST.get('last_name')
            billings.phone = request.POST.get('phone')
            billings.payment_code = request.POST.get('payment_code')
            billings.country = request.POST.get('country')
            billings.city = request.POST.get('city')
            billings.region = request.POST.get('region')
            billings.street = request.POST.get('street')
            billings.apartment = request.POST.get('apartment')
            billings.zip_code = request.POST.get('zip_code')
            billings.delivery_price = request.POST.get('delivery_price')
            billings.discount_price = request.POST.get('discount_price')
            billings.delivery_date_time = request.POST.get('delivery_date_time')
            billings.client_gave_money = request.POST.get('client_gave_money')
            billings.change_price = request.POST.get('change_price')
            billings.total_price = request.POST.get('total_price')

            billings.save()
            return redirect('orders')
        
    return render(request, 'applications/products/orders/orders_detail.html', {
                'title': title,
                'users': users,
                'billings': billings,
                'billing_type_choices':Billing.BillingTypeChoices.choices,
                'billing_receipt_type_choices':Billing.BillingReceiptTypeChoices.choices,
                'billing_payment_status':Billing.BillingPaymentStatusChoices.choices,
                'billing_payment':Billing.BillingPaymentChoices.choices,
                'billing_status':Billing.BillingStatusChoices.choices,
            })

@require_POST
def delete_billing(request, billing_id):
    if not request.user.is_authenticated:  
        return JsonResponse({"success": False, "error": "Пользователь не авторизован."})

    try: 
        billing = Billing.objects.get(id=billing_id)
        billing.delete()  
        return JsonResponse({'success': True})  
    except Billing.DoesNotExist:
        return JsonResponse({'success': False, 'error': "Товар не найден."})  


def order_detail(request, order_id):
    title = "Детали биллинга"
    get_billing = get_object_or_404(Billing, id=order_id)
    users = User.objects.all()  
    
    return render(request, 'applications/products/orders/detail.html', locals())
