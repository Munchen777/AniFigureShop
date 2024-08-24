from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from decimal import Decimal


from products.serializers import ProductSerializer
from products.models import Product
from orders.models import OrderItem
from .mixins import CartMixin
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CreateCartAPIView(APIView, CartMixin):
    permission_classes = [AllowAny]
    def post(self, request: Request) -> Response:
        # # print("сработал метод post")
        # print(f"{request.data=}")
        # product = request.data["product"]
        # quantity = request.data["quantity"]

        # # Валидация данных продукта
        # serializer = ProductSerializer(data=product)
        # serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data)
        # product_id = serializer.validated_data["pk"]

        # # Находим товар в БД
        # try:
        #     product = Product.objects.get(pk=product_id)
        # except Product.DoesNotExist:
        #     return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # # Если юзер аутентифицирован
        # if request.user.is_authenticated:
        #     print("пользователь аутентифицирован")
        #     cart, created = Cart.objects.get_or_create(user=request.user)
        # else:
        #     print("пользователь не аутентифицирован")
        #     session_key = request.session.session_key
        #     cart, created = Cart.objects.get_or_create(session_key=session_key)
        # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # if not created:
        #     cart_item.quantity = quantity
        # else:
        #     cart_item.quantity += quantity

        # cart_item.save()
        # cart_item_serializer = CartItemSerializer(cart_item)
        # print(cart_item_serializer.data)

        # return Response({"msg": "successfully added to cart!",
        #                  "cart_item": cart_item_serializer.data}, status=status.HTTP_202_ACCEPTED)

        print("сработал метод post")
        # print(f"{request.data=}")
        product = request.data["product"]
        quantity = request.data["quantity"]

        # Валидация данных продукта
        product_serializer = ProductSerializer(data=product)
        product_serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data)
        product_id = product_serializer.validated_data["pk"]
  
        # Находим товар в БД
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product_id = str(product_id)

        session = request.session.get("cart", {})
        print(f"{session=}")

        if product_id in session:
            session[product_id]["quantity"] += quantity
            print(session[product_id]["quantity"])
            if session[product_id]["quantity"] <= 0:
                del session[product_id]
        else:
            session[product_id] = {
                "product": product_serializer.data,
                "quantity": quantity
            }
        
        request.session["cart"] = session
        request.session.modified = True

        print(f"{request.session["cart"]=}")
        # request.session["cart"] = session

        # request.session["cart"] = session
        cart_items = [
            {
             "product": item["product"],
             "quantity": item["quantity"]
            }
            for item in request.session["cart"].values()
            ]
        # request.session.modified = True  # сообщаем Django, что сессия была изменена

        print(f"{cart_items=}")

        cart_item_serializer = CartItemSerializer(cart_items, many=True)
        print(f"{cart_item_serializer.data}")
        
        return Response({"msg": "cart item successfully added to cart!",
                         "cart": cart_item_serializer.data}, status=status.HTTP_200_OK)
    

def post_test(self, request, *args, **kwargs):
    request.session['test_key'] = 'test_value'
    test_value = request.session.get('test_key')
    print(f"test_value={test_value}")
    return Response({"msg": "Test completed"}, status=status.HTTP_200_OK)
            
            
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
        
