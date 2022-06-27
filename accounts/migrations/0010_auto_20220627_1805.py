# Generated by Django 3.1.13 on 2022-06-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220627_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(default='https://web.facebook.com', max_length=255, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkein',
            field=models.CharField(default='https://www.linkedin.com/', max_length=255, verbose_name='LinkeIn'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(default='https://twitter.com/', max_length=255, verbose_name='Twitter'),
        ),
    ]
