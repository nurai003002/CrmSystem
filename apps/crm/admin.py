from django.contrib import admin

from apps.crm import models
# Register your models here.

class TeamPeopleTabularInline(admin.TabularInline):
    model = models.TeamPeople
    extra = 2

@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'description')
    list_filter = ('id', 'task')

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')

@admin.register(models.TeamPerson)
class TeamPersonAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_filter = ('id', )
    inlines = (TeamPeopleTabularInline, )
