from django.contrib import admin

from .models import Banner


@admin.action(description="Сделать баннер неактивным")
def make_banner_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Сделать баннер активным")
def make_banner_inactive(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "content",
        "is_active",
        "start_date",
        "end_date",
    ]
    actions = (
        make_banner_inactive,
    )
