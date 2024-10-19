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
