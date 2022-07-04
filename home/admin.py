from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from home.models import Enroll, Event, Blog, Tag


class EventAdmin(SummernoteModelAdmin):
    exclude = ('slug',)
    summernote_fields = ('event_descrip')


class TagAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class BlogAdmin(SummernoteModelAdmin):
    exclude = ('slug',)
    summernote_fields = ('blog_descrip')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Enroll)
admin.site.register(Event, EventAdmin)
admin.site.register(Tag, TagAdmin)
