from django.urls import path

from apps.products import views

urlpatterns = [
    # ecommerce
    path('product/', views.products, name='products'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.customers, name='customers'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shops/', views.shops, name='shops'),
    path('add-product/', views.add_product, name='add_product'),
    
]