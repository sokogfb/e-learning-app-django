# Generated by Django 3.1.13 on 2022-04-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_del_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='currency',
            field=models.CharField(default='K', max_length=3, verbose_name='Currency'),
        ),
    ]
