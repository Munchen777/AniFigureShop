from drf_spectacular.utils import (extend_schema,
                                   extend_schema_view
                                   )
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Request, Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny


from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


@extend_schema(tags=["Товары"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список товаров с изображениями"
    ),
    create=extend_schema(
        summary="Создать новый товар"
    )
)
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    # def get(self, request: Request) -> Response:
    #     products = Product.objects.filter(archived=False)
    #     serialized = ProductSerializer(products, many=True)
    #     return Response({"products": serialized.data})


@extend_schema(tags=["Категории товаров"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все категории"
    ),
    create=extend_schema(
        summary="Создать новую категорию"
    ),
    destroy=extend_schema(
        summary="Удалить категорию товара"
    )
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
