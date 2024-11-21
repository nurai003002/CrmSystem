from django.db import models

from apps.users.models import User

# models.py в приложении chats
class Room(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название комнаты'
    )
    topic = models.CharField(
        max_length=255,
        verbose_name='Тема'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class ChatMessage(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, 
        related_name='messages',
        blank=True, null=True
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        verbose_name='Отправитель',
        related_name='sent_messages',
        blank=True, null=True
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name = 'Получатель',
        blank=True, null=True
    )
    content = models.TextField(
        verbose_name='Сообщение'
    )
    timestamp = models.TimeField(
        auto_now_add=True,
        blank=True, null=True
    )
    is_read = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content[:20]}"
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['timestamp'] 
