from django.urls import path
from rest_framework import routers


# from .views import CreateCartAPIView
from .views import CreateCartAPIView


app_name = "carts"

carts_router = routers.DefaultRouter()

# carts_router.register("purchase", PurchaseProductAPIView, basename="PurchaseProductAPIView")

urlpatterns = [
    # path("purchase/", CreateCartAPIView.as_view(), name="purchase"),
]
# urlpatterns = carts_router.urls
