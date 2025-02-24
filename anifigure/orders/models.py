from django.db import models
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """
    Model of Order

    Attributes:
        user - FK to User model
        promocode - promocode for order
        delivery_address - delivery address for order
        created_at - time when the order was created
        requires_delivery - whether order's required delivery
        phone_number - phone number for order
        status - status of order
        is_paid - whether order's paid
    
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True,
        verbose_name="User",
    )
    promocode = models.CharField(
        max_length=40,
        blank=True,
        verbose_name="Promocode",
    )
    delivery_address = models.TextField(
        null=True,
        blank=True,
        verbose_name="Delivery address",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
    )
    requires_delivery = models.BooleanField(
        default=False,
        verbose_name="Delivery required",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Phone number",
    )
    status = models.CharField(
        default="В обработке",
        max_length=100,
        verbose_name="Status"
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="Is paid",
    )

    class Meta:
        db_table = 'order'
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


class OrderItem(models.Model):
    """
    Model of OrderItem
    
    Attributes:
        order - FK to Order model
        product - FK to Product model
        price - price of order item
        quantity - quantity of order item
        created_at - time when it's ordered
    
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order"
    )
    product = models.ForeignKey(
        Product, 
        n_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name="Product",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Quantity",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
    )

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"
