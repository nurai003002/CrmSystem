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

    # ecommerce
    path('products/', views.products, name='products'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.customers, name='customers'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shops/', views.shops, name='shops'),
    path('add-product/', views.add_product, name='add_product'),
]