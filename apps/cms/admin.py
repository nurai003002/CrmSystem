from django.contrib import admin

from apps.cms.models import Slider, Services, Calendar, FAQ
# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_1', 'description_1')
    list_filter = ('id', 'title_1')

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('id', 'event')
    list_filter = ('id', 'event')
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_filter = ('id', 'question')
