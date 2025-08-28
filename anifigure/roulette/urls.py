from django.urls import path
from . import views

urlpatterns = [


    path("bonuses/", views.bonuses_page_view, name="bonuses"),
    path("bonuses/<slug:bonus_slug>/", views.promotion_page_view, name="promotion"),


    path("random-category/", views.random_category_view, name="random-category"),
    path('random-category/save_bonus/', views.save_roulette_bonus, name='save_roulette_bonus'),




]

