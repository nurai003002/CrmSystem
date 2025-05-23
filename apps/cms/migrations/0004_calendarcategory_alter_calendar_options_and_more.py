# Generated by Django 5.0.6 on 2024-11-18 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_status_name', models.CharField(max_length=500, verbose_name='Название катеория')),
            ],
            options={
                'verbose_name': 'Событие (Календарь)',
                'verbose_name_plural': 'Событие (Календарь)',
            },
        ),
        migrations.AlterModelOptions(
            name='calendar',
            options={'verbose_name': 'Планы (Календарь)', 'verbose_name_plural': 'Планы (Календарь)'},
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='event_name',
        ),
        migrations.AddField(
            model_name='calendar',
            name='event',
            field=models.CharField(default=1, max_length=500, verbose_name='Событие'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calendar',
            name='calendar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='calendar_event', to='cms.calendarcategory', verbose_name='Выберите категорию'),
            preserve_default=False,
        ),
    ]
