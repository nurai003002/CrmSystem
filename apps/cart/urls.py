from django.urls import path

from apps.cart.views import cart, add_to_cart, remove_from_cart

urlpatterns = [ 
    path('', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]