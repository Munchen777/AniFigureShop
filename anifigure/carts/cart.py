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

            self.queryset = Cart.objects.filter(user=self.user) # Находим корзину пользователя
            cart = self.get_cart_from_db(self.queryset) # Находим корзину в бд

        else:
            if not cart:
                # save an empty cart in session
                cart = self.session[settings.CART_SESSION_ID] = {}
            print(f"Текущая корзина анонима: {cart}")
        print(self.use_db)
        self.cart = cart

    def get_cart_from_db(self, qs):
        print("сработал метод get_cart_from_db")
        cart = {}
        for item in qs:
            cart[str(item.product.pk)] = {'product': item.product, 'quantity': item.quantity}

        print(f"{cart=} из метода get_cart_from_db")
        return cart

    def save(self):
        print("сработал метод save")
        if not self.use_db:
            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.modified = True
            print("сессия модифицирована: ", self.session[settings.CART_SESSION_ID])

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
            update_quantity: bool = False
            ):
        # Получаем продукт
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

            if not update_quantity:
                cart.quantity = quantity
            else:
                cart.quantity += quantity

            cart.save()

        else:
            product_id = str(product.pk)
            if product_id not in self.cart:
                self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'product': product_serializer.data
                }
            if not update_quantity:
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


## Try to implement
# class _Cart:
#     """
#     A Basket class with different storage mechanisms depending on user authentication.
#     """

#     def __init__(self, request):
#         self.session = request.session
#         self.user = request.user

#         if self.user.is_authenticated:
#             self.basket = self.get_user_basket_items()
#         else:
#             basket = self.session.get('skey')
#             if 'skey' not in request.session:
#                 basket = self.session['skey'] = {}
            
#             print("Текущая корзина: ", basket)
#             self.basket = basket

#     def get_user_basket_items(self):
#         """
#         Retrieves basket items from the database for an authenticated user.
#         """
#         return {
#                 str(item.product.id):
#             {
#                 'price': str(item.product.price),
#                 'quantity': item.quantity
#             }
#             for item in Cart.objects.filter(user=self.user)
#                }

#     def add(self,
#             product_serializer: ProductSerializer,
#             quantity : int = 1,
#             updateQuantity: bool = False
#             ):
#         """
#         Adding and updating the user's basket session or database data
#         """
#         product_id = str(product_serializer.data["pk"])
#         product = Product.objects.get(pk=int(product_id))

#         if self.user.is_authenticated:
#             cart, created = Cart.objects.get_or_create(user=self.user, product=product)
            
#             if not updateQuantity:
#                 cart.quantity = quantity
#             else:
#                 cart.quantity += quantity

#             cart.save()

#         else:
#             if product_id in self.basket:
#                 self.basket[product_id]['quantity'] += quantity
#             else:
#                 self.basket[product_id] = {
#                     'price': str(product.price),
#                     'quantity': quantity,
#                     'product': product_serializer.data
#                     }

#             self.save()
            
#         return self.basket

#     def __iter__(self):
#         """
#         Collect the product_id in the session data or database to query the products
#         """
#         if self.user.is_authenticated:
#             basket_items = Cart.objects.filter(user=self.user)
#             for item in basket_items:
#                 yield {
#                     'product': item.product,
#                     'price': str(item.product.price),
#                     'quantity': item.quantity,
#                     'total_price': str(item.product.price) * item.quantity
#                 }
#         else:
#             product_ids = self.basket.keys()
#             products = Product.objects.filter(id__in=product_ids)
#             basket = self.basket.copy()

#             for product in products:
#                 basket[str(product.id)]['product'] = product

#             for item in basket.values():
#                 item['price'] = str(item['price'])
#                 item['total_price'] = item['price'] * item['qty']
#                 yield item

#     def __len__(self):
#         """
#         Get the basket data and count the qty of items
#         """
#         if self.user.is_authenticated:
#             return Cart.objects.filter(user=self.user).count()
#         else:
#             return sum(item['quantity'] for item in self.basket.values())

#     def update(self, product, qty):
#         """
#         Update values in session data or database
#         """
#         product_id = str(product.id)

#         if self.user.is_authenticated:
#             try:
#                 basket_item = Cart.objects.get(user=self.user, product=product)
#                 basket_item.quantity = qty
#                 basket_item.save()
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             if product_id in self.basket:
#                 self.basket[product_id]['quantity'] = qty
#             self.save()

#     def get_total_price(self):
#         """
#         Calculate total price from session data or database
#         """
#         if self.user.is_authenticated:
#             return sum(Decimal(item.product.price) * item.quantity for item in Cart.objects.filter(user=self.user))
#         else:
#             return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

#     def delete(self, product):
#         """
#         Delete item from session data or database
#         """
#         product_id = str(product.id)

#         if self.user.is_authenticated:
#             try:
#                 basket_item = Cart.objects.get(user=self.user, product=product)
#                 basket_item.delete()
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             if product_id in self.basket:
#                 del self.basket[product_id]
#             self.save()

#     def save(self):
#         if not self.user.is_authenticated:
#             self.session["skey"] = self.basket
#             self.session.modified = True
