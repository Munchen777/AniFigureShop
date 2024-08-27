from django.conf import settings
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


from products.serializers import ProductSerializer


class Cart:
    def __init__(self,
                 request: Request
                 ):
        bearer_token: str = request.headers.get("Authorization", None)
        access_token = bearer_token.split()[-1]

        # try:
        #     token = AccessToken(access_token)
        # except TokenError:
        #     return Res

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self,
            product_serializer: ProductSerializer,
            quantity: int=1
            ):
        """Добавляем товар в корзину, если его нет, иначе изменяем количество

        Args:
            product_serializer (ProductSerializer): сериализатор Продуктов
            quantity (int, optional): Количество продукта. Defaults to 1.
        """
        product_id = str(product_serializer.validated_data["pk"])

        print(f"Текущая корзина: {self.cart=}")
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
            print(self.cart[product_id]["quantity"])
            if self.cart[product_id]["quantity"] <= 0:
                del self.cart[product_id]
        else:
            self.cart[product_id] = {
                "product": product_serializer.data,
                "quantity": quantity
            }
        self.save()

        return self.cart

        
        
