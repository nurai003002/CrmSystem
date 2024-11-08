from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from apps.crm import models as crm_models
from apps.users.models import User
def todo(request):
    title = 'Задачи'
    tasks_list = crm_models.Todo.objects.all()
    users = User.objects.all()
    status = crm_models.Todo.objects.values_list('status', flat=True).distinct() 

    if request.method == 'POST':
        if 'new_task' in request.POST:
            data = {
                'task': request.POST.get('task'),
                'description': request.POST.get('description'),
                'status': request.POST.get('status'),
                'date': request.POST.get('date'),
                'user': crm_models.User.objects.get(id=request.POST.get('users')) if request.POST.get('users') else None, 
            }

            tasks = crm_models.Todo(**data)
            tasks.save()
            return redirect('todo')
            
    return render(request, 'applications/app/todo/todo.html', 
                  {'title': title,
                    'status_choices': crm_models.Todo.STATUS_CHOICES,
                   'users': users,
                   'tasks_list': tasks_list,
                   })

def todo_detail(request, task_id):
    title = 'Детальный'
    task = get_object_or_404(crm_models.Todo, id=task_id)
    users = User.objects.all()
    categories = crm_models.Todo.STATUS_CHOICES

    if request.method == 'POST':
        if 'save_task' in request.POST:
            # Обновляем данные задачи
            task.task = request.POST.get('task')
            task.description = request.POST.get('description')
            task.status = request.POST.get('choices_category')
            task.date = request.POST.get('date')
            task.user = User.objects.get(id=request.POST.get('users'))
            task.save()
            return redirect('todo')  # Возвращаемся к списку задач после сохранения

        elif 'delete_task' in request.POST:
            # Удаление задачи
            task.delete()
            return redirect('todo')

    return render(request, 'applications/app/todo/todo_detail.html', {
        'title': title,
        'task': task,
        'users': users,
        'categories': categories,
    })