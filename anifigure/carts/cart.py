from django.conf import settings
from django.db import transaction
from rest_framework.request import Request


from carts.models import Cart
from products.models import Product
from products.serializers import ProductSerializer


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


class _Cart:
    def __init__(self,
                 request: Request
                 ):
        self.use_db = False
        print(f"{request.user.is_authenticated=}")
        self.session = request.session
        self.user = request.user
        self.queryset = None

        cart = self.session.get(settings.CART_SESSION_ID)

        if self.user.is_authenticated:
            self.use_db = True
            if cart:
                print(f"Текущая корзина пользователя: {cart=}")
                self.save_db(cart, self.user)

            self.queryset = Cart.objects.filter(user=self.user)
            cart = self.get_cart_from_db(self.queryset)

        else:
            if not cart:
                # save an empty cart in session
                cart = self.session[settings.CART_SESSION_ID] = {}
            print(f"Текущая корзина анонима: {cart}")

        self.cart = cart

    def get_cart_from_db(self, qs):
        print("сработал метод get_cart_from_db")
        cart = {}
        for item in qs:
            cart[str(item.product.pk)] = {'product': item.product, 'quantity': item.quantity}

        print(f"{cart=} из метода get_cart_from_db")
        return cart

    def save(self):
        if not self.use_db:
            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.modified = True

    def save_db(self, cart: dict, user):
        print("сработал метод save_db")
        for key, value in cart.items():
            if Cart.objects.filter(user=user, product=product).exists():
                product = Cart.objects.select_for_update().get(user=user, product=product)
                product.quantity += cart[key]["quantity"]
                product.price = cart[key]["price"]
                product.save()
            else:
                product = Product.objects.get(pk=key)
                Cart.objects.create(
                    user=user,
                    product=product,
                    quantity=value["quantity"]
                )

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        # cart = self.cart.copy()

        for product in products:
            self.cart[str(product.pk)]["product"] = ProductSerializer(product).data
        for item in self.cart.values():
            item["price"] = str(item["price"])
            item["total_price"] = str(item["price"] * item["quantity"])
            yield item

    def add(self,
            product_serializer: ProductSerializer,
            quantity: int = 1,
            update_quantity: bool = True
            ):
        print("срботал метод add")
        product_pk = product_serializer.data["pk"]
        product = Product.objects.get(pk=product_pk)

        if self.use_db:
            if self.queryset.filter(product=product).exists():
                with transaction.atomic():
                    cart = self.queryset.select_for_update().get(product=product)
            else:
                cart = Cart(
                    user=self.user,
                    product=product,
                    quantity=0,
                    # price=product.price
                )

            if update_quantity:
                cart.quantity = quantity
            else:
                cart.quantity += quantity

            cart.save()

        else:
            product_id = str(product.pk)
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity': 0, 'price': str(product.price), "product": product_serializer.data}
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity

            self.save()

        # product_id = str(product_serializer.validated_data["pk"])
        # print(product_serializer.validated_data)

        # print(f"Текущая корзина: {self.cart=}")
        # if product_id in self.cart:
        #     print("товар в корзине")
        #     self.cart[product_id]["quantity"] += quantity
        #     print(self.cart[product_id]["quantity"])
        #     if self.cart[product_id]["quantity"] <= 0:
        #         del self.cart[product_id]
        # else:
        #     print("товара нет в корзине")
        #     self.cart[product_id] = {
        #         "product": product_serializer.data,
        #         "quantity": quantity
        #     }
        # self.save()

        return self.cart
