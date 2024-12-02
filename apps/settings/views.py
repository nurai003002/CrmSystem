from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta, date

from apps.settings.models import Sales
from apps.billings.models import BillingProduct
# Create your views here.

# dashboard
def index(request):
    title = 'Главная'
    today = date.today()
    week_ago = today - timedelta(days=7)

    # Фильтруем завершенные биллинги
    completed_billings = BillingProduct.objects.filter(status=True)

    # Общая сумма продаж
    total_sales = completed_billings.aggregate(total=Sum('total'))['total'] or 0

    # Продажи за текущую и прошлую неделю
    sales_this_week = completed_billings.filter(created__range=(week_ago, today)).aggregate(
        total=Sum('total')
    )['total'] or 0

    sales_last_week = completed_billings.filter(created__range=(week_ago - timedelta(days=7), week_ago)).aggregate(
        total=Sum('total')
    )['total'] or 0

    # Процент изменения
    percent_change = ((sales_this_week - sales_last_week) / sales_last_week * 100) if sales_last_week else 0

    # Данные для графика (продажи по дням за последнюю неделю)
    daily_sales = completed_billings.filter(created__range=(week_ago, today)).values('created').annotate(
        daily_total=Sum('total')
    )
    sales_data = [day['daily_total'] for day in daily_sales]
    

    return render(request, 'applications/dashboard/index.html', locals())


def sales_data(request, period):
    # Получаем данные о продажах за текущий период
    if period == 'yearly':
        start_date = now() - timedelta(days=365)
    elif period == 'monthly':
        start_date = now() - timedelta(days=30)
    elif period == 'weekly':
        start_date = now() - timedelta(days=7)
    else:  # today
        start_date = now() - timedelta(days=1)
    
    sales_current_period = BillingProduct.objects.filter(
        created__gte=start_date
    ).aggregate(total_sales=Sum('total'))['total_sales'] or 0

    # Получаем данные о продажах за предыдущий период
    previous_sales = get_previous_sales_data(period)

    # Вычисляем процент изменения
    percentage = calculate_percentage(sales_current_period, previous_sales)

    # Получаем данные для графика
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
    # Определяем дату начала предыдущего периода
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
