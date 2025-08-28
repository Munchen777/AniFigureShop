from django.conf import settings
from django.db import models


class Category(models.Model):
    """
    Model of Category

    Attributes:
        parent_category - parent category of subcategory
        name - name of category
        description - the description of category
        slug - category slug
        category_image - image of category
    
    """
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Category parent",
    )
    name = models.CharField(
        max_length=80,
        verbose_name="Category name",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Category description",
    )
    slug = models.SlugField(
        max_length=80,
        unique=True,
        db_index=True,
        default=name,
        verbose_name="Category slug",
    )
    category_image = models.ImageField(
        upload_to="categories/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Category image",
    )


class Product(models.Model):
    """
    Model of Product

    Attributes:
        category - FK to Category model
        created_by - FK to User model
        name - name of product
        description - description of product
        price - price of product
        slug - product slug
        discount - product discount
        archived - whether product is archieved or not
        available - whether product is available or not
        updated_at - time when the product instance was updated
        created_at - time when the product instance was created
        quantity - quantity of product

    """
    CURRENCY_CHOICES = (
        ("$", "dollar"),
        ("€", "euro"),
        ("£", "pound"),
        ("₽", "ruble"),
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Product category",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Product created by",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Product name"
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="Product description",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Product price",
    )
    slug = models.SlugField(
        max_length=80,
        unique=True,
        db_index=True,
        verbose_name="Product slug",
    )
    discount = models.SmallIntegerField(
        default=0,
        verbose_name="Product discount",
    )
    archived = models.BooleanField(
        default=False,
        verbose_name="Product archived",
    )
    available = models.BooleanField(
        default=True,
        verbose_name="Product available",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Product updated at",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Product created at",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Quantity of product",
    )
    currency = models.CharField(
        null=True,
        blank=True,
        choices=CURRENCY_CHOICES,
        verbose_name="Currency of product price"
    )

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * (self.discount / 100), 2)

        return self.price

    def __str__(self):
        return f"Product №{self.pk} | {self.name}"


def product_images_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename
    )


class ProductImage(models.Model):
    """
    Model of ProductImage
    
    Attributes:
        product - FK to Product model
        image - image of define product

    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to=product_images_directory_path,
        default=None,
        blank=True,
        null=True,
        verbose_name="Product Image",
    )
