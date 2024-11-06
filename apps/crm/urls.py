from django.urls import path

from apps.crm.views1 import todo_views

urlpatterns = [
    # todo
    path('todo/', todo_views.todo, name='todo'),
]