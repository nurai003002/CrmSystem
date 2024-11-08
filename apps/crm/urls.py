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
    # contacts
    path('contacts/grid/', grid_users_views.contact_grid, name='contacts_grid'),
    path('contacts/list/', grid_users_views.contact_list, name='contacts_list'),
    path('contacts/profile/', grid_users_views.contacts_profile, name='contacts_profile'),
]