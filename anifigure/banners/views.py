from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from .models import Banner
from .serializers import BannerSerializer


class GetBannersAPIView(ModelViewSet):
    queryset = Banner.objects.filter(is_active=True).all()
    serializer_class = BannerSerializer
    permission_classes = (AllowAny, )
