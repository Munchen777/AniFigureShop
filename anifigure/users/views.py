from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from products.models import ProductImage
from users.models import CartItem
from users.forms import LoginUserForm, RegisterForm
from users.serializers import UserLoginSerializer


@method_decorator(csrf_protect, name="dispatch")
class LoginAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request: Request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email", None)
        username = serializer.validated_data.get("username", None)
        password = serializer.validated_data.get("password", None)
        print(email, username, password)
        user = authenticate(username=email or username, password=password)

        print(user)

        if user:
            login(request=request, user=user)
            
            return Response({"data": serializer.validated_data, "message": "Успешный логин"}, status=status.HTTP_200_OK)

        return Response({"message": "Неправильные credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    permission_classes = (AllowAny, )

    def get(self, request: Request):
        return Response({"success": "CSRF cookie is set"})


class LoginTemplateView(TemplateView):
    template_name = "index.html"


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')




def logout_user(request):
    logout(request)
    return redirect("users:login")


def cart_items(request):
    user = request.user
    user_cart_items = CartItem.objects.filter(user=user)

    cart_items_with_product_info = []

    for cart_item in user_cart_items:
        product = cart_item.product
        product_images = ProductImage.objects.filter(product=product)
        cart_items_with_product_info.append(
            {'cart_item': cart_item, 'product': product, 'product_images': product_images})

    return render(request, 'users/cart.html',
                  {'cart_items_with_product_info': cart_items_with_product_info, 'title': "Корзина"})


def profile_user(request):
    return render(request, 'users/profile.html', context={"title": "Профиль"})
