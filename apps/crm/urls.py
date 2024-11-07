from django.urls import path

from apps.crm.views1 import todo_views

urlpatterns = [
    # todo
    path('todo/', todo_views.todo, name='todo'),
    path('todo_detail/<int:task_id>/', todo_views.todo_detail, name='todo_detail'),
]