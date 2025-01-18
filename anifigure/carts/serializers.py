from rest_framework import serializers

from products.serializers import ProductSerializer
from orders.models import OrderItem
from .models import Cart


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = [
            "product",
            "quantity",
        ]
