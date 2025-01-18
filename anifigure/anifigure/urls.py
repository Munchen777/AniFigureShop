from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)

from users.serializers import MyTokenObtainPairView
from base.views import page_not_found


urlpatterns = [
    path("", include("base.urls", namespace="base")),
    path("", include("users.urls", namespace="users")),
    path("", include("carts.urls")),
    path("", include("products.urls")),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("admin/", admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
