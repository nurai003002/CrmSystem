from django.contrib import admin
from apps.users.models import User, UserExperience, UserProject, UserPost, UserComment

class UserExperienceTabularInline(admin.TabularInline):
    model = UserExperience
    extra = 2

class UserProjectTabularInline(admin.TabularInline):
    model = UserProject
    extra = 2

class UserPostTabularInline(admin.TabularInline):
    model = UserPost
    extra = 1

class UserCommentTabularInline(admin.TabularInline):
    model = UserComment
    fk_name = 'profile'
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email')
    inlines = (UserExperienceTabularInline, UserProjectTabularInline, 
               UserPostTabularInline, UserCommentTabularInline)
    