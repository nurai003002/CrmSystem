# Generated by Django 5.0.6 on 2024-11-20 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_chatmessage_room_alter_chatmessage_sender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='room',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
