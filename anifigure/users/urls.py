from django.urls import path
from . import views
from .views import GetCSRFToken

app_name = 'users'

urlpatterns = [
    path("csrf_cookie/", GetCSRFToken.as_view()),
    path("api/login/", views.LoginAPIView.as_view(), name="login"),
    path("login/", views.LoginTemplateView.as_view()),    
    path("logout/", views.logout_user, name="logout"),
    path("registration/", views.RegisterUser.as_view(), name="registration"),
    path("profile/", views.profile_user, name="profile"),

    path("cart/", views.cart_items, name="cart"),

]

