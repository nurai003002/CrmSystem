# Generated by Django 5.0.6 on 2024-11-15 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_reset_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reset_code',
        ),
    ]
