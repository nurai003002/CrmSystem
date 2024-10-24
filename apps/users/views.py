from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
import json

from apps.users.models import User
# contacts
def register(request):
    title = "Регистрация"
    if request.method == "POST":
        if 'register_button' in request.POST:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            errors = {}

            if User.objects.filter(username=username).exists():
                errors['username'] = 'Пользователь с таким именем уже существует.'

            if User.objects.filter(email=email).exists():
                errors['email'] = 'Пользователь с таким email уже существует.'

            if len(password) < 8:
                errors['password'] = 'Пароль должен содержать не менее 8 символов.'

            if errors: 
                return JsonResponse({'success': False, 'errors': errors})

            user = User(username=username, email=email)
            user.password = make_password(password)
            user.save()

            return redirect('index')
    return render(request, 'pages/users/register.html', locals())

def login_view(request):
    title = "Войти" 
    if request.method == 'POST':
        if 'login_button' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return JsonResponse({'success': False, 'error': 'Неправильное имя пользователя или пароль'})

    return render(request, 'pages/users/login.html', locals())

def logout_view(request):
    logout(request)
    return redirect('user_login')

# def logout(request):
#     title = "Выйти"
#     return render(request, 'pages/users/logout.html', locals())

def contact_grid(request):
    return render(request, 'applications/contacts/grid.html', locals())

def contact_list(request):
    return render(request, 'applications/contacts/list.html', locals())

def contacts_profile(request):
    return render(request, 'applications/contacts/profile.html', locals())

