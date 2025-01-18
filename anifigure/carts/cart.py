from collections import defaultdict
from django.conf import settings
from django.db import transaction
from django.db.models import QuerySet
from django.contrib.sessions.models import Session
from rest_framework.request import Request
from typing import List

from carts.models import Cart
from products.models import Product
from products.serializers import ProductSerializer


class _Cart:
    """
    Корзина товаров

    Атрибуты:
        self.user - пользователь
        self.use_database - используем ли базу данных
        self.session - сессия

    """
    def __init__(self, request: Request):
        self.user = request.user
        self.queryset = None
        self.use_database: bool = False
        self.session: Session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if self.user.is_authenticated:
            self.use_database = True
            if cart:
                self.save_in_database(cart)
                self.clear(True)

            self.queryset = Cart.objects.filter(user=self.user)
            cart = self.get_cart_from_database(self.queryset)

        else:
            if not cart:
                # сохранить пустую корзину в сеансе
                cart = self.session[settings.CART_SESSION_ID] = {}

        print(f"Найденная ранее корзина: {cart = }")
        self.cart = cart

    def get_cart_from_database(self, queryset: QuerySet[Cart]):
        cart = {}

        for item in queryset:
            cart[str(item.product.pk)] = {
                "product": item.product,
                "quantity": item.quantity
            }

        return cart

    def save(self):
        if not self.use_database:
            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.modified = True

    def clear_session(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save_in_database(self, cart: dict):
        print(f"{cart = }")

        for key, value in cart.items():
            if Cart.objects.filter(user=self.user, product=key).exists():
                with transaction.atomic():
                    product = Cart.objects.select_for_update().get(
                        user=self.user,
                        product=key
                    )
                    product.quantity += cart[key]["quantity"]
                    product.save()

            else:
                product = Product.objects.get(pk=key)
                Cart.objects.create(
                    user=self.user,
                    product=product,
                    quantity=value["quantity"]
                )

    def __iter__(self):
        if self.use_database:
            print(f"{self.cart.items() = }")

            for item in self.cart.values():
                item['total_price'] = item['price'] * item['quantity']
                print(f"{item = }")
                yield item
        
        else:
            product_ids: List = self.cart.keys()
            products = Product.objects.filter(pk__in=product_ids)

            for product in products:
                self.cart[str(product.pk)]["product"] = ProductSerializer(product).data

            for item in self.cart.values():
                item["price"] = str(item["price"])
                item["total_price"] = str(item["price"] * item["quantity"])
                yield item

    def add(
        self,
        serializer: ProductSerializer,
        quantity: int = 1,
    ):
        product_pk = str(serializer.data["pk"])
        product = Product.objects.get(pk=product_pk)

        if self.use_database:
            cart, created = Cart.objects.get_or_create(
                user=self.user,
                product=product,
            )
            # Если кол-во товара <= 0
            if quantity <= 0:
                cart.delete()

            # Если корзина не была создана, то обновляем количество
            else: # if not created
                cart.quantity = quantity
                cart.save()

            # else:
            #     cart.save()

            self.queryset = Cart.objects.filter(user=self.user)
            self.cart = self.get_cart_from_database(self.queryset)

        else:
            print(f"Корзина неаутентифицированного пользователя: {self.cart}")
            if product_pk in self.cart:
                self.cart[product_pk]["quantity"] = quantity

                if self.cart[product_pk]["quantity"] <= 0:
                    del self.cart[product_pk]

            else:
                self.cart[product_pk] = {
                    "product": serializer.data,
                    "quantity": quantity,
                }

            self.save()

        return self.cart

    def get_cart(self):
        return self.cart
        if self.user.is_authenticated:
            # Получаем корзину пользователя
            return self.cart
            # cart = Cart.objects.get(user=self.user)
            # cart_products = cart.products.all()
            # print(cart_products)
        
        else:
            return self.cart

    def clear(self, only_session):
        if only_session:
            self.clear_session()

        else:
            if self.queryset:
                self.queryset.delete()
