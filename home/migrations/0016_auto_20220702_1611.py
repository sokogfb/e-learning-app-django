# Generated by Django 3.1.13 on 2022-07-02 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220702_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 2, 14, 11, 12, 884211, tzinfo=utc), verbose_name='Event End Time'),
        ),
    ]
