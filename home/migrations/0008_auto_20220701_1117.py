# Generated by Django 3.1.13 on 2022-07-01 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220701_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 1, 9, 17, 10, 551236, tzinfo=utc), verbose_name='Event End Time'),
        ),
    ]
