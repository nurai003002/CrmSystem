from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
import json, random
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

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

def check_user_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'is_authenticated': True})
    else:
        return JsonResponse({'is_authenticated': False})
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Некорректные данные'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            if not User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'error': 'Неверное имя пользователя', 'field': 'username'})
            else:
                return JsonResponse({'success': False, 'error': 'Неверный пароль', 'field': 'password'})
    
    
    return render(request, 'pages/users/login.html', locals())

def logout_view(request):
    logout(request)
    return redirect('user_login')

# pages/auth
def recoverpw(request):
    if request.method == 'POST':
        if 'reset_password' in request.POST:
            email = request.POST.get('email')
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Пользователь с таким email не найден.'})

            reset_code = random.randint(1000, 9999)

            request.session['reset_email'] = email
            request.session['reset_code'] = reset_code

            send_mail(
                'Сброс пароля',
                f'Ваш код для сброса пароля: {reset_code}',
                'noreply@yourdomain.com',
                [email],
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Код отправлен на вашу почту.'})
        
            
    return render(request, 'pages/auth/recoverpw.html', locals())

def lock_screen(request):
    return render(request, 'pages/auth/lock-screen.html', locals())

def confirm_mail(request):
    return render(request, 'pages/auth/confirm-mail.html', locals())

def verification(request):
    return render(request, 'pages/auth/verification.html', locals())

def two_verification(request):
    if request.method == 'POST':
        entered_code = ''.join([
            request.POST.get('digit1'),
            request.POST.get('digit2'),
            request.POST.get('digit3'),
            request.POST.get('digit4')
        ])
        stored_code = request.session.get('reset_code')
        email = request.session.get('reset_email')

        if str(entered_code) == str(stored_code):
            return redirect('new_password')
        else:
            return render(request, 'pages/auth/two-verification.html', {
                'error': 'Неверный код. Попробуйте снова.'
            })

    return render(request, 'pages/auth/two-verification.html')


def new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.session.get('reset_email')  
        
        if new_password != confirm_password:
            return render(request, 'pages/auth/new_password.html', {
                'error': 'Пароли не совпадают.'
            })

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)  
            user.save()

            login(request, user)

            return redirect('index')
        except User.DoesNotExist:
            return render(request, 'pages/auth/new_password.html', {
                'error': 'Пользователь не найден.'
            })

    return render(request, 'pages/auth/new_password.html')