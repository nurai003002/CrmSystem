from django.shortcuts import render

# Create your views here.

# dashboard
def index(request):
    return render(request, 'applications/dashboard/index.html', locals())

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
