from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound

from base.models import Category, Product


def page_not_found(request, exception):
    return HttpResponseNotFound("Ne naidena brat")


def anime_category_view(request):
    categories = Category.objects.filter(parent_category=1)
    print(categories)
    data = {
        "title": "AniShop: Аниме",
        "categories": categories,
    }
    return render(request, 'base/anime_category.html', context=data)


def anime_category_products_view(request, category_slug):
    chosen_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=chosen_category)

    data = {
        "title": category_slug,
        "products": products,

    }
    return render(request, 'base/product_card.html', context=data)


def anime_products_view(request, category_slug, product_slug):
    products = Product.objects.filter(slug=product_slug)

    data = {
        "title": product_slug,
        "products": products,

    }
    return render(request, 'base/product.html', context=data)


def random_category_view(request):
    data = {
        "title": "AniShop: Рандом",
    }
    return render(request, 'base/random_category.html', context=data)


def estetic_category_view(request):
    data = {
        "title": "AniShop: Эстетика",
    }
    return render(request, 'base/estetic_category.html', context=data)


def main_page(request):
    return HttpResponse("main page")


def base_view(request):
    data = {
        "title": "AniShop",
    }
    return render(request, 'base/base.html', context=data)
