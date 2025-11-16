from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'username')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address', 'date_of_birth', 'created_at']
    search_fields = ['user__email', 'phone']
    list_filter = ['created_at', 'date_of_birth']


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
