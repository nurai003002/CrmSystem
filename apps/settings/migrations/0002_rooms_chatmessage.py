# Generated by Django 5.0.6 on 2024-11-19 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название комнаты')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255, verbose_name='Отправитель')),
                ('content', models.TextField(verbose_name='Само сообщение')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='settings.rooms')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
