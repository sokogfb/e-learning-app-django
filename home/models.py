from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django_countries.fields import CountryField

from accounts.models import User
from courses.models import Course


class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolls')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)


class Tag(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=350, unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:tag_index", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_head_pic = models.ImageField(verbose_name='Head Picture', upload_to='event/events/headers')
    event_title = models.CharField(verbose_name='Title', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    event_descrip = models.TextField(verbose_name='Description')
    event_country = CountryField(blank_label='(select country)')
    event_city = models.CharField(verbose_name='Town/City', max_length=75)
    event_date = models.DateField(verbose_name='Event Date')
    event_start_time = models.TimeField(verbose_name='Event Start Time')
    event_end_time = models.TimeField(verbose_name='Event End Time', default=now())
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.event_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_title)
        super(Event, self).save(*args, **kwargs)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_head_pic = models.ImageField(verbose_name='Head Picture', upload_to='event/events/headers', default=None)
    blog_title = models.CharField(verbose_name='Title', max_length=50, default=None)
    slug = models.SlugField(max_length=200, unique=True, default=None)
    blog_descrip = models.TextField(verbose_name='Description', default=None)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title)
        super(Blog, self).save(*args, **kwargs)
