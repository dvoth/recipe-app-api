from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # convention for converting strings to readable text

from core import models

class UserAdmin(BaseUserAdmin):
    # test case: test_users_listed
    ordering = ['id']
    list_display = ['email', 'name']

    # test case: test_user_change_page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    # test case: test_create_user_page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )



admin.site.register(models.User, UserAdmin)