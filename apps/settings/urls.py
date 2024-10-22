from django.urls import path

from apps.settings import views

urlpatterns = [
    # applications
    path('', views.index, name='index'),
    path('sale/', views.sales, name='sales'),
    path('calendar/', views.calendar, name='calendar'),
    path('todo/', views.todo, name='todo'),
    path('manager/', views.manager, name='manager'),
    path('chat/', views.chat, name='chat'),
    
    # invoices
    path('invoices/list/', views.invoice_list, name='invoice_list'),
    path('invoices/detail/', views.list_detail, name='list_detail'),
    
    # components/tables
    path('components/basic-tables/', views.basic_table, name='basic_table'),
    path('components/advanced-tables/', views.advanced_table, name='advanced_table'),

    # components/charts
    path('components/charts-apex/', views.charts_apex, name='charts_apex'),
    path('components/charts-chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('components/charts-tui/', views.charts_tui, name='charts_tui'),
    
    # maps
    path('components/maps-google/', views.maps_google, name='maps_google'),

    # pages/auth
    path('auth/recoverpw/', views.recoverpw, name='recoverpw'),
    path('auth/lock-screen/', views.lock_screen, name='lock_screen'),
    path('auth/confirm_mail/', views.confirm_mail, name='confirm_mail'),
    path('auth/verification/', views.verification, name='verification'),
    path('auth/two-verification/', views.two_verification, name='two_verification'),

    # pages/utility
    path('utility/timeline/', views.timeline, name='timeline'),
    path('utility/faqs/', views.faqs, name='faqs'),
    path('utility/404/', views.pages_404, name='pages_404'),
    path('utility/pages_500/', views.pages_500, name='pages_500'),
    path('utility/pricing/', views.pricing, name='pricing'),

]   