# Generated by Django 5.0.6 on 2024-10-24 12:24

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_remove_productreview_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=40, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/', verbose_name='Фото изделий')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена сейчас')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвета')),
                ('size', models.CharField(blank=True, default='S', max_length=100, null=True, verbose_name='Размер товара')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество заказанного продукта')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена товаров')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]
