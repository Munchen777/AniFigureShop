from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from products.serializers import ProductSerializer
from products.models import Product
from orders.models import OrderItem
from .cart import _Cart
from .mixins import CartMixin
from .serializers import CartSerializer, CartItemSerializer


class CartAddAPIView(APIView, CartMixin):
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request: Request) -> Response:
        print("сработал метод post")
        product = request.data["product"]
        quantity = request.data["quantity"]

        # Валидация данных продукта
        product_serializer = ProductSerializer(data=product)
        product_serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data)
        # product_id = str(product_serializer.validated_data["pk"])

        cart = _Cart(request)
        cart_with_products = cart.add(product_serializer, quantity)
        print(f"{cart.cart=}")

        # # Находим товар в БД
        # try:
        #     product = Product.objects.get(pk=product_id)
        # except Product.DoesNotExist:
        #     return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        print(f"{cart_with_products=}")
        cart_items = [
            {
             "product": val["product"],
             "quantity": val["quantity"]
            }
            for val in cart_with_products.values()
            ]

        cart_item_serializer = CartItemSerializer(cart_items, many=True)
        print(f"{cart_item_serializer.data=}")

        return Response({"msg": "cart item successfully added to cart!",
                         "cart": cart_item_serializer.data}, status=status.HTTP_200_OK)

            
        # session = request.session

        # product_data = serializer.validated_data
        # for key, value in product_data.items():
        #     if isinstance(value, Decimal):
        #         product_data[key] = float(value)

        # if "cart" not in session:
        #     session["cart"] = {}

        # cart = session["cart"]
        # print(f"Current session cart before modification: {session.get('cart', {})}")

        # if str(product_id) in cart:
        #     print("cart item находится в корзине")
        #     cart[str(product_id)]["quantity"] += quantity
        #     if cart[str(product_id)]["quantity"] <= 0: # ?
        #         del cart[str(product_id)] # ?
        #         session.modified = True

        #     print(f"{cart[str(product_id)]=}")

        # else:
        #     print("cart item нет в корзине!")
        #     cart[str(product_id)] = {
        #         "product": product_data,
        #         "quantity": quantity,
        #     }

        # session["cart"] = cart
        # session.modified = True
        # print(f"{session["cart"]=}")
        # return Response({"msg": "cart item successfully added to cart!",
        #                  "cart": session["cart"]}, status=status.HTTP_202_ACCEPTED)
        
