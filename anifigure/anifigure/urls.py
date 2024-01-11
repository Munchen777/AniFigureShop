from django.contrib import admin
from django.urls import include, path
from base.views import page_not_found

urlpatterns = [
    path("", include("base.urls")),
    path("admin/", admin.site.urls),
]

handler404 = page_not_found
