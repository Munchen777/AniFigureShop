from django.urls import path
from . import views

urlpatterns = [
    path("", views.base_view, name="main"),

    path("bonuses/", views.bonuses_page_view, name="bonuses"),
    path("bonuses/<slug:bonus_slug>/", views.promotion_page_view, name="promotion"),


    path("random-category/", views.random_category_view, name="random-category"),
    path('random-category/save_bonus/', views.save_roulette_bonus, name='save_roulette_bonus'),

    path("estetic-category/", views.estetic_category_view, name="estetic-category"),
    path("estetic-category/<slug:category_slug>/", views.estetic_products_view, name="estetic-product"),


    path("anime-category/", views.anime_category_view, name="anime-category"),
    path("anime-category/<slug:category_slug>/", views.anime_category_products_view, name="anime-baby-category"),
    path("anime-category/<slug:category_slug>/<slug:product_slug>", views.anime_products_view, name="anime-product"),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),





]

