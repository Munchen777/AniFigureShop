from django.urls import path

from .views import CartListView
from .views import CartAPIView

app_name = "carts"


urlpatterns = [
    path("api/v1/cart/get/", CartListView.as_view(), name="cart-get"),
    path("api/v1/cart/update/", CartAPIView.as_view(), name="cart-update"),
]
