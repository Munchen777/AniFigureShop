from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from anifigure import settings
from products.views import page_not_found

urlpatterns = [

    path("", include("products.urls")),
    path("", include("roulette.urls")),
    path("", include("users.urls")),
    path("", include("order.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found