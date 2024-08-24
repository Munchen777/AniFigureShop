from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Request, Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny


from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    # def get(self, request: Request) -> Response:
    #     products = Product.objects.filter(archived=False)
    #     serialized = ProductSerializer(products, many=True)
    #     return Response({"products": serialized.data})


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
