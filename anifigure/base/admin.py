from django.contrib import admin
from .models import Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'category_image', 'description', 'slug', 'order']
