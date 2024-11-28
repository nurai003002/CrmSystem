from django.urls import path

from apps.products import views


urlpatterns = [
    # ecommerce
    path('product/', views.products, name='products'),
    path('product_list/', views.products_list, name='products_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.customers, name='customers'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-category/', views.add_category, name='add_category'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    
]