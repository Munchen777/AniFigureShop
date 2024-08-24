from django.urls import path


from .views import RegisterAPIView, LoginAPIView


app_name = 'users'


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    # path("login/", views.LoginUser.as_view(), name="login"),
    # path("logout/", views.logout_user, name="logout"),
    # path("register/", views.RegisterUser.as_view(), name="registration"),
    # path("profile/", views.profile_user, name="profile"),
    # path("cart/", views.cart_items, name="cart"),
    
]
