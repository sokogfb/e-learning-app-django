# Generated by Django 3.1.13 on 2022-06-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220627_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='linkein',
            new_name='linkedin',
        ),
    ]
