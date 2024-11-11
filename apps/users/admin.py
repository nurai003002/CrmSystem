from django.contrib import admin
from apps.users.models import User, UserExperience, UserProject

class UserExperienceTabularInline(admin.TabularInline):
    model = UserExperience
    extra = 2

class UserProjectTabularInline(admin.TabularInline):
    model = UserProject
    extra = 2

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email')
    inlines = (UserExperienceTabularInline, UserProjectTabularInline)
    