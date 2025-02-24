from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@extend_schema(tags=["Товары"])
@extend_schema_view(
    list=extend_schema(summary="Получить список товаров с изображениями"),
    create=extend_schema(summary="Создать новый товар"),
)
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related("images").all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )


@extend_schema(tags=["Категории товаров"])
@extend_schema_view(
    list=extend_schema(summary="Получить все категории"),
    create=extend_schema(summary="Создать новую категорию"),
    destroy=extend_schema(summary="Удалить категорию товара"),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )
