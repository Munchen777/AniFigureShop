from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import (extend_schema,
                                   extend_schema_view
                                   )


from products.serializers import ProductSerializer
from products.models import Product
from orders.models import OrderItem
from .cart import _Cart
from .mixins import CartMixin
from .serializers import CartSerializer, CartItemSerializer


@extend_schema(
    summary="Endpoint для работы с корзиной товаров"
)
class CartAddAPIView(APIView, CartMixin):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        update_quantity = request.data["updateQuantity"]
        product = request.data["product"]
        quantity = request.data["quantity"]

        # Валидация данных продукта
        product_serializer = ProductSerializer(data=product)
        product_serializer.is_valid(raise_exception=True)

        cart = _Cart(request)
        cart_with_products = cart.add(
            product_serializer=product_serializer,
            quantity=quantity,
            update_quantity=update_quantity
            )

        cart_items = [
            {
             "product": value["product"],
             "quantity": value["quantity"]
            }
            for value in cart_with_products.values()
            ]

        cart_item_serializer = CartItemSerializer(cart_items, many=True)

        return Response({"msg": "cart item successfully added to cart!",
                         "cart": cart_item_serializer.data}, status=status.HTTP_200_OK)
