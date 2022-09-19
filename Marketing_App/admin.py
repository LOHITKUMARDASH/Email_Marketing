from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
import logging
logger = logging.getLogger(__name__)
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser
    list_display = ('id', 'user_name',)
    ordering = ('user_name',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', '', 'country', 'state', 'Address','is_credit', 'admin_id')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_super', 'is_admin', 'is_client')}),
        ('Personal', {'fields': ('password1',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                 'user_name', 'email', 'first_name', 'password', 'is_staff','is_active', 'is_super', 'is_admin', 'is_client')}
         ),
    )


admin.site.register(NewUser)
admin.site.register(product)
admin.site.register(invoice_settings)
admin.site.register(fileuploads)
admin.site.register(Invoice)
admin.site.register(group)
admin.site.register(template)
admin.site.register(customers)

