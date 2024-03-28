from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("registration/", views.RegisterUser.as_view(), name="registration"),
    path("profile/", views.profile_user, name="profile"),

    path("cart/", views.cart_items, name="cart"),

]

