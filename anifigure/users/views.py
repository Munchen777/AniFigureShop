from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from products.models import ProductImage
from users.models import CartItem
from users.forms import LoginUserForm, RegisterForm


# Class-Based View для аутентификации пользователя
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
