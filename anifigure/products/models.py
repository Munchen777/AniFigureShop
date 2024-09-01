from django.conf import settings
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name="Category name")
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Category parent")
    description = models.TextField(blank=True, verbose_name="Category description")
    slug = models.SlugField(max_length=80, unique=True, db_index=True, default=name, verbose_name="Category slug")
    category_image = models.ImageField(upload_to="categories/", default=None, blank=True, null=True,
                                       verbose_name="Category image")


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product name")
    description = models.TextField(verbose_name="Product description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Product category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product price")
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name="Product slug")
    discount = models.SmallIntegerField(default=0, verbose_name="Product discount")
    archived = models.BooleanField(default=False, verbose_name="Product archived")
    available = models.BooleanField(default=True, verbose_name="Product available")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name="Product created by")
    updated_at = models.DateTimeField(verbose_name="Product updated at", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Product created at", auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity of product")

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * (self.discount / 100), 2)

        return self.price


def product_images_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_images_directory_path, default=None, blank=True, null=True,
                              verbose_name="Product Image")
