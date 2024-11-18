from django.shortcuts import render, redirect

from apps.settings.models import Setting
from apps.cms.models import Calendar

def calendar(request):
    title = 'Календарь'
    setting = Setting.objects.latest('id')
    
    return render(request, 'applications/app/apps-calendar.html', locals())
