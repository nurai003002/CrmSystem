from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from apps.users.models import User

def contact_grid(request):
    title = "Пользователи"
    users = User.objects.all()
    paginator = Paginator(users, 10)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    
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
        
    return render(request, 'applications/contacts/grid/grid.html',
                  {'title': title,
                   'users': users,
                   'user_count': user_count,
                   'page_obj': page_obj,
                    'stack_choices': User.STACK})

def grid_detail(request, grid_id):
    title = "Информация пользователя"
    user = get_object_or_404(User, id=grid_id)  

    if request.method == 'POST':
        if 'data_user' in request.POST:
            user.username = request.POST.get('username')
            user.full_name = request.POST.get('full_name')
            user.stack = request.POST.get('stack')
            user.bio = request.POST.get('bio')
            user.email = request.POST.get('email')
            user.phone = request.POST.get('phone')
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save() 
            return redirect('contacts_grid')
    
    return render(request, 'applications/contacts/grid/grid_detail.html', {
        'title': title,
        'user': user,
        'stack_choices': User.STACK
    })
    
def delete_item(request, user_id):
    item = get_object_or_404(User, id=user_id)
    item.delete()
    return redirect('contacts_grid') 

def contacts_profile(request, get_user_id):
    title = "Профиль"
    get_user = User.objects.get(id=get_user_id)

    return render(request, 'applications/contacts/profile.html', {
        'title': title,
        'get_user': get_user,
    })

def contact_list(request):
    return render(request, 'applications/contacts/list.html', locals())
