from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from drf_spectacular.utils import (extend_schema,
                                   extend_schema_view
                                   )


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.token_blacklist.models import (BlacklistedToken,
                                                             OutstandingToken)


from api.models import User
from products.models import Product
from .serializers import UserSerializer, UserLoginSerializer
from users.managers import CustomUserManager
# from users.models import CartItem
from users.forms import LoginUserForm, RegisterForm


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    print(f"{str(refresh)=} {str(refresh.access_token)=}")
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@extend_schema(
    summary="Регистрирует нового пользователя",
    description=(
        "Данный эндпоинт предназначен для регистрации нового пользователя."
    ),
    request=UserSerializer,
    responses={201: Response},
    methods=["POST"],
)
class RegisterAPIView(APIView):
    """
    View for registration new user

        POST /users/register/

    """
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = get_tokens_for_user(user)
        return Response(
            data=(
                serializer.data,
                {
                    "msg": "registration successfully!",
                    "token": token,
                }),
            status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Логин пользователя",
    description=(
        "Аутентифицируем пользователя по JWT токену.",
        "Если у пользователя токен валидный, то возвращается ответ со статус кодом 200",
        "Если у пользователя токен невалидный или истек, возвращаем ответ со статус кодом 401",
        "В случае, когда у пользователя нет токена, то находим его и отдаем токены"
    ),
    auth=["JWT Authentication"],
    tags=["Пользователи"],
)
class LoginAPIView(APIView):
    """
    View for login user

        POST /users/login/

    """
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        bearer_token = request.headers.get("Authorization", None)
        print("access токен", bearer_token)
        if bearer_token:
            print("получен jwt токен")
            try:
                access_token = bearer_token.split()[-1]
                token = AccessToken(access_token)
                user = token["user_id"]
                print(user)
                print("токен прошел проверку успешно! User:", user)
                return Response({"msg": "User is already authenticated"}, status=status.HTTP_200_OK)
            except TokenError as error:
                return Response({"msg": "Invalid or expired token", "error": str(error)}, status=status.HTTP_401_UNAUTHORIZED)

        print("сработал метод post у метода UserLoginAPIView")
        serializer = UserLoginSerializer(data=request.data)
        # print("валидируем User Login")
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email", None)
        username = serializer.validated_data.get("username", None)
        password = serializer.validated_data.get("password", None)
        print(email, username, password)
        user = authenticate(username=email or username, password=password)
        # print(user)
        if user:
            token = get_tokens_for_user(user)
            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(key="jwt", value=token, httponly=True)
            response.data = {
                "msg": "login successfully!",
                "token": token,
            }
            return response

            # return response({"msg": "login successfully!", "token": token}, status=status.HTTP_200_OK)

        return Response({"msg": "error with login"}, status=status.HTTP_404_NOT_FOUND)




















        # email = request.data.get("email", None)
        # password = request.data["password"]
        # username = request.data.get("username", None)
        # print(username, email, password)

        # user: CustomUserManager[User] = User.objects.filter(email=email).first() \
        #                                 or User.objects.filter(username=username).first()

        # if not user:
        #     raise AuthenticationFailed("User hasn't been found!")

        # if not user or not user.check_password(password):
        #     raise AuthenticationFailed("Invalid credentials!")

        # try:
        #     outstanding_tokens = OutstandingToken.objects.filter(user=user, blacklistedtoken__isnull=True).first()
        #     if outstanding_tokens:
        #         print("токен еще существует")
        #         refresh = RefreshToken(outstanding_tokens.token)
        #         return Response({
        #             "msg": "Login with existing tokens successfully!",
        #             "token": {
        #                 "refresh": str(refresh),
        #                 "access": str(refresh.access_token),
        #             }
        #         },
        #             status=status.HTTP_200_OK)

        # except TokenError:
        #     pass

        # tokens = get_tokens_for_user(user)

        # return Response({"msg": "Login with new tokens", "token": tokens})
        
        
        
        
        
        
        
        
        
        
        
        

        # token = get_tokens_for_user(user)

        # return Response({"msg": "successfully logged in!", "token": token})
    
    
        # serializer = UserLoginSerializer(data=...)
        # if serializer.is_valid(raise_exception=True):
        #     return Response(serializer.data, status=status.HTTP_200_OK)

        # return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    # def post(self, request: Request) -> Response:
    #     email = request.data.get("email", None)
    #     password = request.data["password"]
    #     username = request.data.get("username", None)

    #     user: CustomUserManager[User] = User.objects.filter(email=email).first() \
    #                             or User.objects.filter(username=username).first()

    #     if not user:
    #         raise AuthenticationFailed("User hasn't been found!")

    #     # if user.email != email:
    #     #     raise AuthenticationFailed("Email isn't correct!")

    #     # if user.username != username:
    #     #     raise AuthenticationFailed("Username isn't correct!")

    #     if not user or not user.check_password(password):
    #         raise AuthenticationFailed("Invalid credentials!")

    #     return Response({"message": "successfully!"})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    # def get_success_url(self):
    #     return reverse_lazy('main')


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


def logout_user(request):
    logout(request)
    return redirect("users:login")


def cart_items(request):
    pass
    # user = request.user
    # user_cart_items = CartItem.objects.filter(user=user)

    # cart_items_with_product_info = []

    # for cart_item in user_cart_items:
    #     product = cart_item.product
    #     product_images = ProductImage.objects.filter(product=product)
    #     cart_items_with_product_info.append(
    #         {'cart_item': cart_item, 'product': product, 'product_images': product_images})

    # return render(request, 'users/cart.html',
    #               {'cart_items_with_product_info': cart_items_with_product_info, 'title': "Корзина"})


def profile_user(request):
    return render(request, 'users/profile.html', context={"title": "Профиль"})
