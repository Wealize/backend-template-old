from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(AuthUserAdmin):
    list_display = [
        'email', 'first_name', 'last_name', 'is_active',
        'get_groups'
    ]
    ordering = ('is_active', 'email')

    def get_groups(self, instance):
        return ', '.join([group.name for group in instance.groups.all()])
    get_groups.short_description = _('Groups')


admin.site.register(User, UserAdmin)
