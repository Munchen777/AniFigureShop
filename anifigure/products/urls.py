from django.urls import path
from .views import ProductsViewSet, CategoryViewSet

app_name = "products"


urlpatterns = [
    path("api/products/", ProductsViewSet.as_view({"get": "list"}), name="products"),
    path("api/categories/", CategoryViewSet.as_view({"get": "list"}), name="categories"),
]
