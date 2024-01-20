from django.contrib import admin
from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'avatar', 'verification_code', 'is_active',)
