from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.utils.timezone import now
from datetime import timedelta, date

from apps.settings.models import Sales
from apps.billings.models import BillingProduct
from apps.users.models import User
from apps.products.models import Products
# Create your views here.

def index(request):
    title = 'Главная'
    popular_products = Products.objects.filter(rating__gte=4)
    loyal_customers = User.objects.annotate(order_count=Count('billing_user')).filter(order_count__gt=0).order_by('-order_count')[:5]
    today = date.today()
    week_ago = today - timedelta(days=7)

    completed_billings = BillingProduct.objects.filter(status=True)

    total_sales = completed_billings.aggregate(total=Sum('total'))['total'] or 0

    sales_this_week = completed_billings.filter(created__range=(week_ago, today)).aggregate(
        total=Sum('total')
    )['total'] or 0

    sales_last_week = completed_billings.filter(created__range=(week_ago - timedelta(days=7), week_ago)).aggregate(
        total=Sum('total')
    )['total'] or 0

    percent_change = calculate_percentage(sales_this_week, sales_last_week)

    daily_sales = completed_billings.filter(created__range=(week_ago, today)).values('created').annotate(
        daily_total=Sum('total')
    )
    sales_data = [day['daily_total'] for day in daily_sales]

    orders_this_week = completed_billings.filter(created__range=(week_ago, today)).count()
    orders_last_week = completed_billings.filter(created__range=(week_ago - timedelta(days=7), week_ago)).count()
    orders_percent_change = calculate_percentage(orders_this_week, orders_last_week)
    orders_direction = "up" if orders_percent_change > 0 else "down"
    orders_color = "success" if orders_percent_change > 0 else "danger"

    visitor_stats_today = get_visitor_stats('today')
    visitors_today = visitor_stats_today['current_count']
    visitors_percent_change = visitor_stats_today['percentage_change']
    visitors_color = 'success' if visitors_percent_change >= 0 else 'danger'
    visitors_direction = 'up' if visitors_percent_change >= 0 else 'down'

    context = {
        'title': title,
        'total_sales': total_sales,
        'sales_this_week': sales_this_week,
        'sales_last_week': sales_last_week,
        'percent_change': percent_change,
        'sales_data': sales_data,
        'orders_this_week': orders_this_week,
        'orders_last_week': orders_last_week,
        'orders_percent_change': orders_percent_change,
        'orders_direction': orders_direction,
        'orders_color': orders_color,
        'visitors_today': visitors_today,
        'loyal_customers': loyal_customers,
        'visitors_percent_change': visitors_percent_change,
        'visitors_color': visitors_color,
        'visitors_direction': visitors_direction,
        'popular_products': popular_products,
    }

    return render(request, 'applications/dashboard/index.html', context)


def get_visitor_stats(period):
    today = now()

    if period == 'yearly':
        start_date = today - timedelta(days=365)
        previous_start_date = start_date - timedelta(days=365)
    elif period == 'monthly':
        start_date = today - timedelta(days=30)
        previous_start_date = start_date - timedelta(days=30)
    elif period == 'weekly':
        start_date = today - timedelta(days=7)
        previous_start_date = start_date - timedelta(days=7)
    else:  # Today
        start_date = today.replace(hour=0, minute=0, second=0, microsecond=0)
        previous_start_date = start_date - timedelta(days=1)

    current_count = User.objects.filter(date_joined__gte=start_date).count()
    previous_count = User.objects.filter(date_joined__gte=previous_start_date, date_joined__lt=start_date).count()

    percentage_change = 0
    if previous_count > 0:
        percentage_change = ((current_count - previous_count) / previous_count) * 100

    return {
        'current_count': current_count,
        'previous_count': previous_count,
        'percentage_change': round(percentage_change, 2),
    }

def get_orders_data(request, period):
    if period == 'yearly':
        start_date = now() - timedelta(days=365)
        previous_start_date = start_date - timedelta(days=365)
    elif period == 'monthly':
        start_date = now() - timedelta(days=30)
        previous_start_date = start_date - timedelta(days=30)
    elif period == 'weekly':
        start_date = now() - timedelta(days=7)
        previous_start_date = start_date - timedelta(days=7)
    else:  
        start_date = now() - timedelta(days=1)
        previous_start_date = start_date - timedelta(days=1)

    current_orders_count = BillingProduct.objects.filter(
        created__gte=start_date
    ).count()

    previous_orders_count = BillingProduct.objects.filter(
        created__gte=previous_start_date,
        created__lt=start_date
    ).count()

    percentage_change = calculate_percentage(current_orders_count, previous_orders_count)

    data = {
        'current_orders_count': current_orders_count,
        'previous_orders_count': previous_orders_count,
        'percentage_change': percentage_change
    }

    return JsonResponse(data)

def sales_data(request, period):
    if period == 'yearly':
        start_date = now() - timedelta(days=365)
    elif period == 'monthly':
        start_date = now() - timedelta(days=30)
    elif period == 'weekly':
        start_date = now() - timedelta(days=7)
    else: 
        start_date = now() - timedelta(days=1)
    
    sales_current_period = BillingProduct.objects.filter(
        created__gte=start_date
    ).aggregate(total_sales=Sum('total'))['total_sales'] or 0

    previous_sales = get_previous_sales_data(period)

    percentage = calculate_percentage(sales_current_period, previous_sales)

    sales_graph = BillingProduct.objects.filter(
        created__gte=start_date
    ).values('created').annotate(total_sales=Sum('total'))
    
    sales_data = [sale['total_sales'] for sale in sales_graph]

    data = {
        'total_sales': sales_current_period,
        'percentage': percentage,
        'sales_graph': sales_data
    }

    return JsonResponse(data)


def get_previous_sales_data(period):
    if period == 'yearly':
        start_date = now() - timedelta(days=365)
        previous_start_date = start_date - timedelta(days=365)
    elif period == 'monthly':
        start_date = now() - timedelta(days=30)
        previous_start_date = start_date - timedelta(days=30)
    elif period == 'weekly':
        start_date = now() - timedelta(days=7)
        previous_start_date = start_date - timedelta(days=7)
    else:  # today
        start_date = now() - timedelta(days=1)
        previous_start_date = start_date - timedelta(days=1)
    
    # Получаем данные о продажах для текущего периода
    sales_current_period = BillingProduct.objects.filter(
        created__gte=start_date
    ).aggregate(total_sales=Sum('total'))['total_sales'] or 0

    # Получаем данные о продажах для предыдущего периода
    sales_previous_period = BillingProduct.objects.filter(
        created__gte=previous_start_date,
        created__lt=start_date
    ).aggregate(total_sales=Sum('total'))['total_sales'] or 0

    return sales_previous_period

def calculate_percentage(total_sales, previous_sales):
    if previous_sales == 0:
        return 0  # Если в предыдущем периоде не было продаж, процент не рассчитывается
    return ((total_sales - previous_sales) / previous_sales) * 100


def sales(request):
    return render(request, 'applications/dashboard/sales.html', locals())

# applications 
def manager(request):
    return render(request, 'applications/app/apps-file-manager.html', locals())


# invoices
def invoice_list(request):
    return render(request, 'applications/invoices/list.html', locals())

def list_detail(request):
    return render(request, 'applications/invoices/detail.html', locals())


#components/tables
def basic_table(request):
    return render(request, 'components/tables/tables-basic.html', locals())

def advanced_table(request):
    return render(request, 'components/tables/tables-advanced.html', locals())

def advanced_table(request):
    return render(request, 'components/tables/tables-advanced.html', locals())

#components/charts
def charts_apex(request):
    return render(request, 'components/charts/apex.html', locals())

def charts_chartjs(request):
    return render(request, 'components/charts/chartjs.html', locals())

def charts_tui(request):
    return render(request, 'components/charts/tui.html', locals())

# maps
def maps_google(request):
    return render(request, 'components/maps/google.html', locals())



# pages/utility
def timeline(request):
    return render(request, 'pages/utility/timeline.html', locals())

def faqs(request):
    return render(request, 'pages/utility/faqs.html', locals())

def pricing(request):
    return render(request, 'pages/utility/pricing.html', locals())

def pages_404(request):
    return render(request, 'pages/utility/pages-404.html', locals())

def pages_500(request):
    return render(request, 'pages/utility/pages-500.html', locals())
