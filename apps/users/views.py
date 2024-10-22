from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from apps.users.models import User
# contacts
def register(request):
    title = "Регистрация"
    if request.method == "POST":
        if 'register_button' in request.POST:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = User(username=username, email=email)
            user.password = make_password(password)

            return redirect('/')

    return render(request, 'pages/users/register.html', locals())

def login(request):
    title = "Войти"
    return render(request, 'pages/users/login.html', locals())

def logout(request):
    title = "Выйти"
    return render(request, 'pages/users/logout.html', locals())

def contact_grid(request):
    return render(request, 'applications/contacts/grid.html', locals())

def contact_list(request):
    return render(request, 'applications/contacts/list.html', locals())

def contacts_profile(request):
    return render(request, 'applications/contacts/profile.html', locals())

