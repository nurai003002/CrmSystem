from django.urls import path

from apps.users import views 
urlpatterns = [
    # pages/users
    path('auth/login/', views.login_view, name='user_login'),
    path('auth/register/', views.register, name='user_register'),
    path('auth/logout/', views.logout_view, name='user_logout'),



]