from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'first_name', 'is_active', 'is_staff', 'is_superuser']