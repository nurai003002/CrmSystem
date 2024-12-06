from django.urls import path

from apps.cms import views

urlpatterns = [
    path('faqs/', views.faqs, name='faqs'),
]