# Generated by Django 3.1.13 on 2022-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220627_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile11.png', null=True, upload_to='users/profiles', verbose_name='Profile Picture'),
        ),
    ]