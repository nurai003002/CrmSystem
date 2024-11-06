from django.shortcuts import render, redirect

from apps.crm import models as crm_models
from apps.users.models import User
def todo(request):
    title = 'Задачи'
    tasks_list = crm_models.Todo.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        if 'new_task' in request.POST:
            data = {
                'task': request.POST.get('task'),
                'description': request.POST.get('description'),
                'status': request.POST.get('status'),
                'date': request.POST.get('date'),
                'user': crm_models.Todo.objects.get(id=request.POST.get('users')) if request.POST.get('users') else None,
                }

            tasks = crm_models.Todo(**data)
            tasks.save()

            return redirect('todo')
        
    return render(request, 'applications/app/apps-todo.html', 
                  {'status_choices': crm_models.Todo.STATUS_CHOICES,
                   'users': users,
                   'tasks_list': tasks_list,
                   })