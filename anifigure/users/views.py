from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.forms import LoginUserForm, RegisterForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}

    # def get_success_url(self):
    #     return reverse_lazy('main')

def registration_user(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form})


def logout_user(request):

    form = RegisterForm()

    return render(request, 'users/register.html', { 'form': form})



def profile_user(request):
    return render(request, 'users/profile.html', context={})