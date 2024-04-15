from django.contrib.auth.models import User
from django.db import models
from base.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"

    @classmethod
    def add_to_cart(cls, user, product, quantity):
        existing_item = cls.objects.filter(user=user, product=product).first()

        if existing_item:
            existing_item.quantity += 1
            existing_item.save()

        else:
            new_item = cls(user=user, product=product, quantity=quantity)
            new_item.save()


