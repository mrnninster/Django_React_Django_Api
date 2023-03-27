from dataclasses import field
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import AccountsModel

# Register your models here.
class AccountModelAdminConfig(UserAdmin):

    search_fields = ('server_name', 'login_id', 'platform',)
    list_filter = ('account_id','server_name', 'login_id', 'platform', 'is_staff', 'is_active','is_superuser',)
    list_filter = ('account_id','server_name', 'login_id', 'platform', 'is_staff', 'is_active','is_superuser',)
    ordering = ('-created_date')

    fieldsets = (
        ('Account Info', {'fields':('account_id','server_name','login_id','platform',)}),
        ('Permissions', {'fields':('is_active','is_staff','is_superuser','groups','user_permissions',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('server_name','login_id','platform','password1','password2','groups','user_permissions',),
        })
    )

admin.site.register(AccountsModel)