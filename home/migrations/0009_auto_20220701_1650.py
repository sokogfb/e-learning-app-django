# Generated by Django 3.1.13 on 2022-07-01 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220701_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 1, 14, 50, 31, 677958, tzinfo=utc), verbose_name='Event End Time'),
        ),
    ]