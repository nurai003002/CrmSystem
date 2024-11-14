from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
import json
from django.views.decorators.csrf import csrf_exempt

from apps.users.models import User

def register(request):
    if request.method == "POST": 
            username = request.POST.get('username')
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            errors = {}
            
            if User.objects.filter(username=username).exists():
                errors['username'] = 'Пользователь с таким именем уже существует.'

            if password != confirm_password:
                errors['password'] = 'Пароли должны совпадать.'

            if User.objects.filter(email=email).exists():
                errors['email'] = 'Пользователь с таким email уже существует.'
            
            if len(password) < 8:
                errors['password'] = 'Пароль должен содержать не менее 8 символов.'
            
            if errors:
                return JsonResponse({'success': False, 'errors': errors})
                
            
            user = User(username=username, email=email, first_name=full_name)
            user.is_staff = True 
            user.password = make_password(password)
            user.save()
            return redirect('index')

    return render(request, 'pages/users/register.html', locals())

@csrf_exempt
def login_view(request):
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

# pages/auth
def recoverpw(request):
    return render(request, 'pages/auth/recoverpw.html', locals())

def lock_screen(request):
    return render(request, 'pages/auth/lock-screen.html', locals())

def confirm_mail(request):
    return render(request, 'pages/auth/confirm-mail.html', locals())

def verification(request):
    return render(request, 'pages/auth/verification.html', locals())

def two_verification(request):
    return render(request, 'pages/auth/two-verification.html', locals())