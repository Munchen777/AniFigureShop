from django.urls import path
from .views import ProductsViewSet, CategoryViewSet

app_name = "products"


urlpatterns = [
    path("api/v1/products/", ProductsViewSet.as_view({"get": "list"}), name="products"),
    path("api/v1/categories/", CategoryViewSet.as_view({"get": "list"}), name="categories"),
]
