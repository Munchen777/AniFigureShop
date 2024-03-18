from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}

    # def get_success_url(self):
    #     return reverse_lazy('main')

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
                # return HttpResponseRedirect(reverse('main'))
    #
    # else:
    #     form = LoginUserForm()
    #
    # return render(request, 'users/login.html', {'form': form})


def registration_user(request):
    pass

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    return HttpResponseRedirect(reverse('users:login'))


def profile_user(request):
    return render(request, 'users/profile.html', context={})