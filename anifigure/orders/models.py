from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


from products.models import Product


class OrderitemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    promocode = models.CharField(max_length=40, blank=True)
    delivery_address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number", blank=True, null=True)
    status = models.CharField(default="В обработке", max_length=100, verbose_name="Status or order")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачен")

    class Meta:
        db_table = 'order'
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

    def __repr__(self) -> str:
        return f"Order № {self.pk}\nUser: {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Order")
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name="Product")
    # name = models.CharField(max_length=200, verbose_name="Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of sell")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    objects = OrderitemQueryset.as_manager()

    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else ""} in cart"
