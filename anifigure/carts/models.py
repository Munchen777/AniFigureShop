from django.db import models
from django.conf import settings

from products.models import Product


class Cart(models.Model):
    """
    Model of Cart

    Attributes:
        user - current user with his/her own cart
        product - FK to Product model
        created_at - the date when the cart was created
        quantity - quantity of define product in cart
    
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="User",
        related_name="cart"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Products",
        related_name="cart",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="The date of adding"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantity",
    )

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Cart of {self.user.email}"
