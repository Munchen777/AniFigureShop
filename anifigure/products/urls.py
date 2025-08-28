from django.urls import path
from .views import (
    ProductsViewSet,
    CategoryViewSet,
    CatalogTemplateView,
)

app_name = "base"


urlpatterns = [
    path("catalog/", CatalogTemplateView.as_view(), name="catalog-template"),
    path("api/v1/products/", ProductsViewSet.as_view({"get": "list"}), name="products"),
    path("api/v1/categories/", CategoryViewSet.as_view({"get": "list"}), name="categories"),
]
