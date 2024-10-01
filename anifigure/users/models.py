from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from products.models import Product
from users.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username or "no name"


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"

    @classmethod
    def add_to_cart(cls, user, product, quantity):
        existing_item = cls.objects.filter(user=user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()

        else:
            new_item = cls(user=user, product=product, quantity=quantity)
            new_item.save()
