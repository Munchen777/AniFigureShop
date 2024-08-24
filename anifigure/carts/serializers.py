from rest_framework import serializers


from products.models import Product
from products.serializers import ProductSerializer
from orders.models import OrderItem
from users.serializers import UserSerializer
from .models import Cart, CartItem

"""

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    # product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Product", related_name="cart")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    session_key = models.CharField(max_length=35, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="The date of adding")

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_product")
    updated_at = models.DateTimeField(verbose_name="Cart item updated at", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Cart item created at", auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

"""


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
