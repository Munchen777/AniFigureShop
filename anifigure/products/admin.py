from django.contrib import admin
from .models import Category, Product, ProductImage


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'category_image', 'description', 'slug', 'order']


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'order']
    inlines = [ProductImageInline]

# Register your models here.
