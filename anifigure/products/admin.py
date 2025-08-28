from django.contrib import admin


from .models import Product, ProductImage, Category


class ProductInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description", "discount", "price"]
    list_display_links = ["pk", "name", "description", "price",]
    inlines = [
        ProductInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "parent_category", "description", "slug"]



