from django.urls import path

from .views import GetBannersAPIView

app_name = "banners"


urlpatterns = [
    path("api/v1/get-banners/", GetBannersAPIView.as_view({"get": "list"}), name="get-banners"),
]
