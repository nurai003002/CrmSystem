from django.urls import path

from apps.crm.views1 import todo_views
from apps.crm.views1 import calendar_views 
from apps.crm.views1 import grid_users_views

urlpatterns = [
    # todo
    path('todo/', todo_views.todo, name='todo'),
    path('todo_detail/<int:task_id>/', todo_views.todo_detail, name='todo_detail'),
    
    # calendar
    path('calendar/', calendar_views.calendar, name='calendar'),

    # contacts/grid/
    path('contacts/grid/', grid_users_views.contact_grid, name='contacts_grid'),
    path('contacts/<int:grid_id>/', grid_users_views.grid_detail, name='grid_detail'),
    path('contacts/delete/<int:user_id>/', grid_users_views.delete_item, name='delete_item'),

    path('contacts/profile/<int:get_user_id>/', grid_users_views.contacts_profile, name='contacts_profile'),
    path('contacts/list/', grid_users_views.contact_list, name='contacts_list'),
]