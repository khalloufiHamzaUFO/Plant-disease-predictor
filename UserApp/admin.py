# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import RUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(BaseUserAdmin):
    # Customize list_display, ordering, and other attributes
    list_display = ('email', 'name', 'is_staff','role')  # Adjust to your fields
    ordering = ('email',)  # Ensure this matches your unique field (e.g., 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password','role')}),
        (_('Personal info'), {'fields': ('name',)}),  # Adjust to your fields
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

# Register the new UserAdmin
admin.site.register(RUser, CustomUserAdmin)