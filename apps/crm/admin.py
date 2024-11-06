from django.contrib import admin

from apps.crm import  models
# Register your models here.

@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'description')
    list_filter = ('id', 'task')
