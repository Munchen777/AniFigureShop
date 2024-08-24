from rest_framework.request import Request


from .models import Cart


class CartMixin:
    def get_cart(self, request: Request, product):
        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            query_kwargs = {"session_key": request.user.session_key}

        if product:
            query_kwargs["product"] = product

        return Cart.objects.filter(**query_kwargs).first()
