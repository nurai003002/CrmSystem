from django.db import models
from django.contrib.auth.models import AbstractUser
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

    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"  