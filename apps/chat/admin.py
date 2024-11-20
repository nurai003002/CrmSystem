from django.contrib import admin

from apps.chat.models import Room, ChatMessage
# Register your models here.

@admin.register(Room)
class RoomBackAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')
    list_filter = ('title', 'topic')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'content', 'timestamp')
    search_fields = ('content',) 