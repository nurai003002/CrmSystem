from django.urls import path

from apps.cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    # path('', views.cart, name='cart'),
]
