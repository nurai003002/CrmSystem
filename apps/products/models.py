from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

from apps.users.models import User

# Create your models here.
# User = get_user_model()

class BigCategory(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название главноного категория'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главная категория'

class Category(models.Model):
    big_category = models.ForeignKey(
        BigCategory, 
        related_name="categories",
        on_delete=models.SET_NULL,
        verbose_name="Выбрать главную категорию",
        blank=True, null=True)
    
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название категория'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Дочерняя категория'
        verbose_name_plural = 'Дочерняя категория'


class Products(models.Model):
    COLOR_CHOICES = (
        ('BLACK', 'BLACK'),
        ('GREEN', 'GREEN'),
        ('WHITE', 'WHITE'),
        ('PURPLE', 'PURPLE'),
        ('BLUE', 'BLUE'),
        ('GRAY', 'GRAY'),
        ('RED', 'RED'),
        ('YELLOW', 'YELLOW')
    )
    STATUS_CHOICES = (
        ('в наличии', 'В наличии'),
        ('нет в наличии', 'нет в наличии'),
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название продукта'
    )
    category = models.ForeignKey(
        Category, related_name="category_products",
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        blank=True, null=True
    ) 
    description = RichTextField(
        verbose_name = 'Описание',
        blank=True, null=True
    )
    color = models.CharField(
        max_length=100, verbose_name="Цвет товара",
        choices=COLOR_CHOICES,
        default="BLACK",
        blank=True, null=True
    )
    is_new = models.BooleanField(default=False)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, default='no_image.jpg',
        upload_to='product_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        verbose_name='Статус',
        blank=True, null=True
    )
    brand = models.CharField(
        max_length = 255,
        verbose_name = 'Бренд'
    )
    material = models.CharField(
        max_length = 255,
        verbose_name = 'Материал'
    )
    cost_price = models.PositiveIntegerField(
        verbose_name="Себестоимость",
        blank=True, null=True
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    old_price = models.PositiveIntegerField(
        verbose_name="Старая цена",
        blank=True, null=True
    )
    quantity = models.IntegerField(
        verbose_name = 'Количество продукта',
        blank=True, null=True
    )
    manufacturer = models.CharField(
        max_length = 255,
        verbose_name = 'Производитель'
    )
    discount = models.PositiveIntegerField(
        verbose_name="Скидка на продукт",
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата создания'
    )

    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,
        related_name="product_image",
        verbose_name="Товар"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, default='no_image.jpg',
        upload_to='product_images/',
        verbose_name="Основная фотография",
    )

    def __str__(self):
        return f"{self.product}"
    
    class Meta:
        verbose_name = "Фотография торава"
        verbose_name_plural = "Фотографии товаров"

class ProductsFeature(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,
        related_name="product_feature",
        verbose_name="Товар"
    )
    feature = models.CharField(
        max_length = 255,
        verbose_name = 'Характеристики товара'
    )

    def __str__(self):
        return f"{self.product} - {self.feature}"
    
    class Meta:
        verbose_name = "Характиристика торава"
        verbose_name_plural = "Характиристики товаров"

# rating = models.PositiveSmallIntegerField(
#         choices=[(i, str(i)) for i in range(1, 6)],
#         verbose_name="Звезды", default=0
#     )
        
class ProductReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_reviews",
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Название товара"
    )
    text = models.TextField(
        verbose_name="Текст для отзыва"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f"Отзыв с {self.user.username} для {self.product.title}"

    class Meta:
        verbose_name = "Отзыв товара"
        verbose_name_plural = "Отзывы товаров"
