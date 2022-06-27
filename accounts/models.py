from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from accounts.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = UserManager()


class UserProfile(models.Model):
    T_CHOICES = (
        ("Mis.", "Mis."),
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
        ("Doctor", "Doctor"),
        ("Ass. Professor", "Ass. Professor"),
        ("Professor", "Professor"),
    )

    user = models.OneToOneField(User, max_length=250, verbose_name='User', default=None, unique=True,
                                on_delete=models.CASCADE)
    title = models.CharField(choices=T_CHOICES, verbose_name='Title', max_length=100, default=None)
    phone = models.CharField(max_length=200, null=True, verbose_name='Phone Number')
    country = CountryField(blank_label='Select Country', null=True, verbose_name='Country')
    city = models.CharField(default='Lusaka', max_length=150, null=True, verbose_name='City/District/Town')
    Institute = models.CharField(max_length=200, null=True, verbose_name='Institute or Company')
    profile_pic = models.ImageField(upload_to="users/profiles", default="profile11.png", null=True, blank=True,
                                    verbose_name='Profile Picture')
    facebook = models.CharField(max_length=255, verbose_name='Facebook', default='https://web.facebook.com')
    twitter = models.CharField(max_length=255, verbose_name='Twitter', default='https://twitter.com/')
    linkedin = models.CharField(max_length=255, verbose_name='LinkeIn', default='https://www.linkedin.com/')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')

    def __str__(self):
        return self.user.email
