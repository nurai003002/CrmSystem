from django.urls import path

from apps.chat.views import chat, chat_message_delete

urlpatterns = [
    path('', chat, name='chat'),
     path('chat/message/delete/<int:message_id>/', chat_message_delete, name='chat_message_delete'),
    # path('chat/<str:room_name>/', chat_views.chat, name='chat_room'),
]