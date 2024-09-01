from rest_framework import serializers


from products.models import Product
from products.serializers import ProductSerializer
from orders.models import OrderItem
from users.serializers import UserSerializer
from .models import Cart, CartItem


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer() # write_only=True

    class Meta:
        model = CartItem
        fields = ["cart", "product", "updated_at", "created_at", "quantity"]
        extra_kwargs = {
            "cart": {"write_only": True, "required": False},
            "product": {"write_only": True},
        }


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = ['session_key', 'user', "quantity", "created_at"]
        extra_kwargs = {
            "user": {"required": False, "write_only": True},
        }
