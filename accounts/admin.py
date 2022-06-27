from django.contrib import admin

from accounts.models import User, UserProfile


class UserProfieAdmin(admin.ModelAdmin):
    list_filter = ('title', 'phone', 'city', 'Institute', 'date_created')
    list_display = ('title', 'phone', 'country', 'city', 'Institute', 'date_created', 'facebook', 'linkedin', 'twitter')
    search_fields = ('phone', 'country', 'city', 'Institute')


class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'username', 'first_name', 'last_name', 'date_joined')
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfieAdmin)
