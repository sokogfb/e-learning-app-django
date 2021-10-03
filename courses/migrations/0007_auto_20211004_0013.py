# Generated by Django 3.1.13 on 2021-10-03 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(9.99)]),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.3), django.core.validators.MaxValueValidator(30.0)]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
