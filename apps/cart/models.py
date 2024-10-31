from django.db import models
from django_resized import ResizedImageField

from apps.products.models import Products
from apps.users.models import User

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE,blank=True, null=True)
    session_key = models.CharField(
        max_length=40,
        null=True, blank=True
    )
    quantity = models.IntegerField(
        verbose_name = 'Количество заказанного продукта',
        blank=True, null=True
    )
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Итоговая цена товаров"
    )
   
    def get_formatted_id(self):
        return f"#SK{self.id:04}"
    
    def __str__(self):
        return f"{self.product.title} - {self.quantity} шт."
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"