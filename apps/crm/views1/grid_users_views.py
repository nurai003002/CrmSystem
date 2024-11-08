from django.shortcuts import render, redirect

from apps.users.models import User

def contact_grid(request):
    title = "Пользователи"
    users = User.objects.all()
    user_count = users.count()
    if request.method in 'POST':
        if 'add_contact' in request.POST:
            data ={
                'username': request.POST.get('username'),
                'stack': request.POST.get('stack'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
            }

            contact = User(**data)
            contact.save()
            return redirect('contacts_grid')
        
    return render(request, 'applications/contacts/grid.html',
                  {'title': title,
                   'users': users,
                   'user_count': user_count,
                    'stack_choices': User.STACK})

def contact_list(request):
    return render(request, 'applications/contacts/list.html', locals())

def contacts_profile(request):
    return render(request, 'applications/contacts/profile.html', locals())
