from django.shortcuts import render
from django.http import HttpResponse

from users.forms import LoginUserForm


def login_user(request):
    form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    return HttpResponse("login")
