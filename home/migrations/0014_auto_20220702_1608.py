# Generated by Django 3.1.13 on 2022-07-02 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220702_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_descrip',
            field=models.TextField(default=None, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_head_pic',
            field=models.ImageField(default=None, upload_to='event/events/headers', verbose_name='Head Picture'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(default=None, max_length=50, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='home.Tag'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 2, 14, 8, 3, 736678, tzinfo=utc), verbose_name='Event End Time'),
        ),
    ]
