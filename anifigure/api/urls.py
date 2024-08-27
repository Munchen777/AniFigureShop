from django.urls import path
from rest_framework import routers


from .views import ProductsViewSet, CategoryViewSet
from carts.views import CartAddAPIView


app_name = "api"

router = routers.DefaultRouter()

router.register("products", ProductsViewSet, basename="products-api")
router.register("categories", CategoryViewSet, basename="categories-api")


urlpatterns = [
    path("carts/purchase/", CartAddAPIView.as_view()),
]

urlpatterns += router.urls
