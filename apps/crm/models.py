from django.db import models

from apps.users.models import User
# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = (
        ('В ожидании', 'В ожидании'),
        ('В работе', 'В работе'),
        ('Завершено', 'Завершено'),
    )
    task = models.CharField(
        max_length = 255,
        verbose_name = 'Задача'
    )
    description = models.CharField(
        verbose_name = "Описание таска"
    )
    status = models.CharField(
        max_length = 255,
        verbose_name = 'Статус выполнения таска',
        choices=STATUS_CHOICES,
        blank=True,null=True
    )
    date = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата выполнения',
        blank=True,null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_todo",
        verbose_name="Пользователь",
        blank=True,null=True
    )

    def __str_(self): 
        return f"{self.task} таск- {self.user.username} -исполнитель"
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
