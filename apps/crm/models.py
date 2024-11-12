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
    date = models.DateField(
        verbose_name = 'Дата выполнения',
        blank=True,null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_todo",
        verbose_name="Пользователь",
        blank=True,null=True
    )

    def __str__(self): 
        return f"{self.task} таск- {self.user.username} -исполнитель"
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Team(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = 'Название команды'
    )
    created_at = models.DateTimeField(
        auto_now_add = True, 
        verbose_name = 'Дата создания'
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class TeamPerson(models.Model):
    team = models.ForeignKey(
        Team, on_delete = models.SET_NULL,
        related_name = 'team',
        verbose_name = 'Выберите команду',
        blank=True, null=True
    )
    
    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'

class TeamPeople(models.Model):
    team = models.ForeignKey(
        TeamPerson, on_delete = models.CASCADE,
        related_name = 'teams',
        verbose_name = 'Выберите команду',
    )
    user = models.ForeignKey(
        User, on_delete = models.CASCADE,
        related_name = 'team_person',
        verbose_name = 'Член команды'
    )
    status = models.CharField(
        max_length = 255,
        verbose_name = 'Статус'
    )

    def __str__(self):
        return self.status

    class Meta:
        unique_together = ('team', 'user')
