from django.conf import settings
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from django.views.generic import TemplateView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import UserRegisterSerializer
from .serializers import SetPasswordSerializer
from .serializers import ResetPasswordRequestSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@extend_schema(
    summary="Регистрирует нового пользователя",
    description=("Данный эндпоинт предназначен для регистрации нового пользователя."),
    request=UserRegisterSerializer,
    responses={201: Response},
    methods=["POST"],
)
class RegisterAPIView(APIView):
    """
    APIView for registration new user

    """
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = get_tokens_for_user(user)
        return Response(
            data=(
                serializer.data,
                {
                    "message": "Registration's successfull!",
                    "token": token,
                },
            ),
            status=status.HTTP_201_CREATED,
        )


class RequestPasswordResetView(GenericAPIView):
    """
    GenericAPIView для отправки ссылки для сброса пароля пользователя
    
    Проверяем введенную почту пользователя. Если находим такого пользователя,
    то генерируем токен и отправляем ссылку на сброс пароля

    """
    permission_classes = (AllowAny, )
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        user = CustomUser.objects.filter(email=email).first()

        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request).domain
            relative_link = reverse(
                "users:reset-password-confirm",
                kwargs={"uidb64": uidb64, "token": token}
            )

            reset_url = "http://" + current_site + relative_link
            # отправляем электронное письмо
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_url}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({"message": "Password reset email sent", "frontend_url": reset_url},
                            status=status.HTTP_200_OK)

        return Response({"error": "Good luck"},
                        status=status.HTTP_200_OK)


class ResetPasswordChangeAPIView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SetPasswordSerializer

    def post(self, request: Request, uidb64: str) -> Response:
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(CustomUser, pk=uid)

        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response(
                {
                    "error": "Good luck!"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get("password1")
        user.set_password(password)
        user.save()

        return Response({"message": "Password reset successful"},
                        status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, request: Request, uidb64: str, token: str) -> Response:
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.filter(pk=uid).first()

            token_generator = PasswordResetTokenGenerator()
            if token_generator.check_token(user, token):
                current_site = get_current_site(request).domain
                relative_link = reverse(
                    "users:reset-password-confirm",
                    kwargs={
                        "uidb64": uidb64,
                        "token": token
                    }
                )

                reset_url = "http://" + current_site + relative_link

                return Response(
                    {
                    "message": "token has passed checking",
                    "uidb64": uidb64,
                    "token": token,
                    "redirect_url": reset_url
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json"
                )

            raise Http404("Token is invalid or is expired")

        except (CustomUser.DoesNotExist, Exception) as error:
            raise error


class PasswordResetSuccessView(TemplateView):
    template_name = "index.html"


class RegisterTemplateView(TemplateView):
    template_name = "index.html"


class LoginTemplateView(TemplateView):
    template_name = "index.html"


class ResetPasswordConfirmTemplateView(TemplateView):
    template_name = "index.html"
