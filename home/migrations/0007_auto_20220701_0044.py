# Generated by Django 3.1.13 on 2022-06-30 22:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220701_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_descrip',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 6, 30, 22, 44, 56, 251840, tzinfo=utc), verbose_name='Event End Time'),
        ),
    ]
