# Generated by Django 5.0.6 on 2024-10-23 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='email',
        ),
    ]
