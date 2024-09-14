from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    promocode = models.CharField(max_length=40)
    delivery_address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    products = models.ManyToManyField(Product, related_name='orders')

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'

    def __repr__(self) -> str:
        return f"Order: {self.pk}\nUser: {self.user.username}"