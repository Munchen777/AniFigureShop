from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .cart import _Cart
from .serializers import CartSerializer
from products.serializers import ProductSerializer


@extend_schema(summary="Endpoint для работы с корзиной товаров")
class CartAPIView(APIView):
    #authentication_classes = []
    permission_classes = (AllowAny, )

    def post(self, request: Request) -> Response:
        product = request.data.get("product")
        quantity = request.data.get("quantity")
        serializer = ProductSerializer(data=product)
        serializer.is_valid(raise_exception=True)

        print(f"{quantity=}")
        cart = _Cart(request)
        cart_with_products = cart.add(
            serializer=serializer,
            quantity=quantity,
        )

        cart_items: list[dict] = [
            {
                "product": ProductSerializer(value["product"]).data,
                "quantity": value["quantity"],
            }
            for value in cart_with_products.values()
        ]

        serializer = CartSerializer(data=cart_items, many=True)
        serializer.is_valid(raise_exception=True)
        print(f"Сериализованная корзина пользователя: {serializer.data}")
        return Response(
            {
                "cart": serializer.data,
                "message": "cart has been updated",
            },
            status=status.HTTP_200_OK,
        )


class CartListView(APIView):
    # authentication_classes = []
    permission_classes = (AllowAny, )

    def get(self, request: Request) -> Response:
        """
        Возвращает корзину пользователя (аутентифицированного или анонимного)

        Атрибуты:
            request (Request): get-запрос

        """
        cart = _Cart(request)
        
        cart_items: list[dict] = [
            {
                "product": ProductSerializer(value["product"]).data,
                "quantity": value["quantity"],
            }
            for value in cart.get_cart().values()
        ]
        print(cart_items)
        serializer = CartSerializer(data=cart_items, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "cart": serializer.data,
                "message": "cart has been retrieved"
            },
            status=status.HTTP_200_OK,
        )
