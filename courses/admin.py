from django.contrib import admin

from .models import Category, Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_filter = ('category', 'language', 'currency', 'user')
    list_display = ('title', 'category', 'language', 'currency', 'user', 'created_at')
    search_fields = ('title', 'category', 'language', 'currency', 'user', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_filter = ('title', 'slug')
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'slug')


class LessonAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_filter = ('title', 'course', 'duration', 'created_at', 'updated_at')
    list_display = ('title', 'course', 'duration', 'created_at', 'updated_at')
    search_fields = ('title', 'course', 'duration')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
