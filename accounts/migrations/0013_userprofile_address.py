# Generated by Django 3.1.13 on 2022-07-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_userprofile_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Address'),
        ),
    ]