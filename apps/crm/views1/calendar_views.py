from django.shortcuts import render, redirect

def calendar(request):
    return render(request, 'applications/app/apps-calendar.html', locals())
