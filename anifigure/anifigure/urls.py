from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from anifigure import settings
from base.views import page_not_found

urlpatterns = [
    path("", include("base.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found