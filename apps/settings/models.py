from django.db import models

from apps.users.models import User

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название Сайта'
    )
    logo = models.ImageField(
        upload_to = 'logo',
        verbose_name = 'Логотип'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основные настройки'
        verbose_name_plural = 'Основные настройки'


class Sales(models.Model):
    date = models.DateField()  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.date}: {self.amount}"