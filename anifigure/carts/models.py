from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


from products.models import Product


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    # product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Product", related_name="cart")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    session_key = models.CharField(max_length=35, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="The date of adding")

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    objects = CartQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self) -> str:
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name if self.product else ""} | Количество {self.quantity}"

        return f"Анонимная корзина | Товар {self.product.name if self.product else ""} | Количество {self.quantity}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_product")
    updated_at = models.DateTimeField(verbose_name="Cart item updated at", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Cart item created at", auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Корзина {self.cart.user.username if self.cart.user else "anonymous user"} | Товар {self.product.name if self.product else ""} | Количество {self.quantity}"
