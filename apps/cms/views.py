from django.shortcuts import render

from apps.cms.models import FAQ
from apps.settings.models import Setting

# Create your views here.
def faqs(request):
    setting = Setting.objects.latest('id')
    faqs = FAQ.objects.all()
    return render(request, 'pages/utility/faqs.html', locals())
