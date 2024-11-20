from django.urls import path

from apps.chat.views import chat

urlpatterns = [
    path('', chat, name='chat'),
    # path('chat/<str:room_name>/', chat_views.chat, name='chat_room'),
]