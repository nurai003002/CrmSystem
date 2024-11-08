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

def chat(request):
    return render(request, 'applications/app/apps-chat.html', locals())

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


# pages/auth
def recoverpw(request):
    return render(request, 'pages/auth/recoverpw.html', locals())

def lock_screen(request):
    return render(request, 'pages/auth/lock-screen.html', locals())

def confirm_mail(request):
    return render(request, 'pages/auth/confirm-mail.html', locals())

def verification(request):
    return render(request, 'pages/auth/verification.html', locals())

def two_verification(request):
    return render(request, 'pages/auth/two-verification.html', locals())

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
