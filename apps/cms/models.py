from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField

# Create your models here.
class Slider(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, default='no_image.jpg',
        upload_to='product_images/',
        verbose_name="Основная фотография",
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название продукта'
    )
    description = RichTextField(
        verbose_name = 'Описание',
        blank=True, null=True
    )
    feature = RichTextField(
        verbose_name = 'Характеристика',
        blank=True, null=True
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    old_price = models.PositiveIntegerField(
        verbose_name="Старая цена",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Services(models.Model):
    title_1 = models.CharField(
        max_length = 255,
        verbose_name = 'Название (доставка)'
    )
    description_1 = models.TextField(
        verbose_name = 'Описание (доставка)'
    )
    title_2 = models.CharField(
        max_length = 255,
        verbose_name = 'Название (Возврат)'
    )
    description_2 = models.TextField(
        verbose_name = 'Описание (Возврат)'
    )
    title_3 = models.CharField(
        max_length = 255,
        verbose_name = 'Название (Поддержка)'
    )
    description_3 = models.TextField(
        verbose_name = 'Описание (Поддержка)'
    )
    title_4 = models.CharField(
        max_length = 255,
        verbose_name = 'Название (Оплата)'
    )
    description_4 = models.TextField(
        verbose_name = 'Описание (Оплата)'
    )

    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
        
        
class Calendar(models.Model):
    STATUS_CHOICES = [
        ('Срочный', 'Срочный'),
        ('Темный', 'Темный'),
        ('Приватный', 'Приватный'),
        ('Встречи', 'Встречи'),
        ('По желанию', 'По желанию'),
        ('Успешно', 'Успешно'),
    ]
    event = models.CharField(
        max_length = 500,
        verbose_name = 'Событие'
    )
    event_status = models.CharField(
        max_length = 255,
        choices = STATUS_CHOICES,
        verbose_name = 'Статус события'
    )

    def __str__(self):
        return self.event
    
    class Meta:
        verbose_name = 'Планы (Календарь)'
        verbose_name_plural = 'Планы (Календарь)'
        

class FAQ(models.Model):
    question = models.CharField(
        max_length = 255,
        verbose_name = 'Вопрос'
    )
    answer = models.TextField(
        verbose_name = 'Ответы',
        blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.question} - {self.answer}"
    
    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'
        