from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser

@admin.register(CustomUser)
class CustomUser(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', "phone_number", 'is_staff')
    list_display_links = list_display
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', "phone_number")
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ("phone_number",)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )