from django.urls import path

from apps.users import views 

urlpatterns = [
    # pages/users
    path('auth/login/', views.login_view, name='user_login'),
    path('auth/register/', views.register, name='user_register'),
    path('auth/logout/', views.logout_view, name='user_logout'),

    
    # pages/auth
    path('auth/recoverpw/', views.recoverpw, name='recoverpw'),
    path('auth/lock-screen/', views.lock_screen, name='lock_screen'),
    path('auth/confirm_mail/', views.confirm_mail, name='confirm_mail'),
    path('auth/verification/', views.verification, name='verification'),
    path('auth/two-verification/', views.two_verification, name='two_verification'),

]
