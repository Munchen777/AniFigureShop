from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "is_active",
        "is_staff"
    ]
    ordering = [
        "username",
        "id"
    ]
