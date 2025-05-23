from django.urls import path

from apps.settings import views

urlpatterns = [
    # applications
    path('', views.index, name='index'),
    path('sale/', views.sales, name='sales'),
    
    path('manager/', views.manager, name='manager'),
    
    # components/tables
    path('components/basic-tables/', views.basic_table, name='basic_table'),
    path('components/advanced-tables/', views.advanced_table, name='advanced_table'),

    # components/charts
    path('components/charts-apex/', views.charts_apex, name='charts_apex'),
    path('components/charts-chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('components/charts-tui/', views.charts_tui, name='charts_tui'),
    
    # maps
    path('components/maps-google/', views.maps_google, name='maps_google'),

    # pages/utility
    path('utility/timeline/', views.timeline, name='timeline'),
    path('utility/404/', views.pages_404, name='pages_404'),
    path('utility/pages_500/', views.pages_500, name='pages_500'),
    path('utility/pricing/', views.pricing, name='pricing'),

]   