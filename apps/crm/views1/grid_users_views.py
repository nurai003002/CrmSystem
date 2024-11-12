from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.users.models import User, UserComment
from apps.crm import models as crm_models

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


@login_required
def contacts_profile(request, get_user_id):
    title = "Профиль"
    get_user = User.objects.get(id=get_user_id)
    post_url = request.build_absolute_uri(reverse('contacts_profile', args=[get_user_id])) 
    
    user_teams = crm_models.TeamPeople.objects.filter(user=get_user)
    team_members = None

    if user_teams.exists():
        team = user_teams.first().team 
        team_members = crm_models.TeamPeople.objects.filter(team=team)

    if request.method == 'POST':
        if 'comments' in request.POST:
            text = request.POST.get('text')
            comment = UserComment(user=request.user, profile=get_user, text=text)
            comment.save()
            return redirect('contacts_profile', get_user_id)
    
    return render(request, 'applications/contacts/profile.html', {
        'title': title,
        'get_user': get_user,
        'post_url': post_url,
        'team_members': team_members, 
    })

def contact_list(request):
    title = "Список пользователей"
    contact_users = User.objects.all()

    paginator = Paginator(contact_users, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'applications/contacts/list.html', {
        'title': title,
        'contact_users': page_obj,  
    })