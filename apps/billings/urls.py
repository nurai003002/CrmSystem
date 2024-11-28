from django.urls import path

from apps.billings import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('orders/detail/<int:order_id>/', views.order_detail, name='orders_detail'),
    path('orders-edit/<int:order_id>/', views.orders_edit, name='orders_edit'),
    path('orders/<int:billing_id>/', views.delete_billing, name='delete_billing'),
]