from django.urls import path

from .views import RegisterAPIView
from .views import RequestPasswordResetView
from .views import RegisterTemplateView
from .views import LoginTemplateView
from .views import ResetPasswordConfirmTemplateView
from .views import ResetPasswordChangeAPIView

app_name = "users"


urlpatterns = [
    path("users/api/v1/register/", RegisterAPIView.as_view(), name="api-register"),
    path("users/api/v1/reset-password/", RequestPasswordResetView.as_view(), name="reset-password"),
    path("users/api/v1/reset-password-confirm/<str:uidb64>/<str:token>/", ResetPasswordConfirmTemplateView.as_view(), name="reset-password-confirm"),
    path("users/api/v1/update-password/<str:uidb64>/", ResetPasswordChangeAPIView.as_view(), name="reset-password-change"),
    
    path("register/", RegisterTemplateView.as_view(), name="register-template"),
    path("login/", LoginTemplateView.as_view(), name="login-template"),

]
