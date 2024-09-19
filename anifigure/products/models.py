from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=80)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=80, unique=True, db_index=True, default=name)
    category_image = models.ImageField(upload_to="categories/", default=None, blank=True, null=True,
                                       verbose_name="Image")
    order = models.IntegerField(default=0, verbose_name='Order')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=80, unique=True, db_index=True)
    order = models.IntegerField(default=0, verbose_name='Order')

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"products/", default=None, blank=True, null=True,
                              verbose_name="Image")

    def __str__(self):
        return f"Image for {self.product.name}"


class UploadToCategory(models.Model):
    file = models.FileField(upload_to='categories/')
