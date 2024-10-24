from django.urls import path

from apps.users import views 
urlpatterns = [
    # pages/users
    path('auth/login/', views.login_view, name='user_login'),
    path('auth/register/', views.register, name='user_register'),
    path('auth/logout/', views.logout_view, name='user_logout'),

    # contacts
    path('contacts/grid/', views.contact_grid, name='contacts_grid'),
    path('contacts/list/', views.contact_list, name='contacts_list'),
    path('contacts/profile/', views.contacts_profile, name='contacts_profile'),

]