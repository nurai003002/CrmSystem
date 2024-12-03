from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.

class User(AbstractUser):
    STACK = [
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Backend Developer', 'Backend Developer'),
    ]
    stack = models.CharField(
        max_length = 255,
        choices = STACK,
        verbose_name = 'Название Стека',
        blank=True, null=True
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='user/image',
        verbose_name='Фото профиля',
        blank=True, null=True
    )
    address = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес',
        blank=True, null=True
    )
    bio = RichTextField(
        verbose_name = 'Биография',
        blank=True, null=True
    )

    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"  

class UserExperience(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_experience",
        verbose_name="Выбрать пользователя"
    )

    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название технологии',
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Опыт пользователя'
        verbose_name_plural = 'Опыт пользователя'

class UserProject(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Complete', 'Complete'),
        ('Waiting', 'Waiting'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_project",
        verbose_name="Выбрать пользователя"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название проекта',
        blank=True, null=True
    )   
    date = models.DateField(
        verbose_name = 'Дата',
        blank=True, null=True
    )
    budget = models.IntegerField(
        verbose_name = 'Бюджет',
        blank=True, null=True
    )   
    status = models.CharField(
        max_length = 255,
        choices=STATUS_CHOICES,
        verbose_name = 'Статус',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class UserPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_post",
        verbose_name="Выбрать пользователя"
    )
    created_at = models.DateField(
        auto_now_add = True,
        verbose_name = 'Дата создания',
        blank=True, null=True
    )
    like = models.PositiveIntegerField(
        verbose_name = 'Лайки',
        blank=True, null=True
    )
    article = models.TextField(
        verbose_name = 'описание поста',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='user_post',
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.article
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class UserComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name="user_comments",
        verbose_name="Пользователь",
        blank=True, null=True
    )
    profile = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="profile_comments",
        verbose_name="оставлен комментарий",
        blank=True, null=True
    ) 
    text = models.TextField(
        verbose_name = 'Комментарий',
        blank=True, null=True
    )
    created = models.DateField(
        auto_now_add = True,
        verbose_name = 'Дата создания',
        blank=True, null=True
    )

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'комментарии'
