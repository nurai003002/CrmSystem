from django.urls import path

from apps.products import views

urlpatterns = [
    # ecommerce
    path('product/', views.products, name='products'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.customers, name='customers'),
    path('checkout/', views.checkout, name='checkout'),
    path('shops/', views.shops, name='shops'),
    path('add-product/', views.add_product, name='add_product'),
    
]