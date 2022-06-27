# Generated by Django 3.1.13 on 2022-06-27 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220627_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, max_length=250, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(choices=[('Mis.', 'Mis.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Doctor', 'Doctor'), ('Ass. Professor', 'Ass. Professor'), ('Professor', 'Professor')], default=None, max_length=100, verbose_name='Title'),
        ),
    ]
