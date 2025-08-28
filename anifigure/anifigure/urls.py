from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)

from users.serializers import MyTokenObtainPairView


urlpatterns = [
    path("", include("base.urls", namespace="base")),
    path("", include("users.urls", namespace="users")),
    path("", include("carts.urls", namespace="carts")),
    path("", include("products.urls", namespace="products")),
    path("", include("banners.urls", namespace="banners")),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
