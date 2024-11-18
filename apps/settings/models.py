from django.db import models

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