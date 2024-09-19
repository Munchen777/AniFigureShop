from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.templatetags.static import static
from django.http import HttpRequest

from products.models import Category, Product, ProductImage


def page_not_found(request, exception):
    return HttpResponseNotFound("Такой страницы еще не существует(")


def anime_category_view(request):
    categories = Category.objects.filter(parent_category=1)
    print(categories)
    data = {
        "title": "AniShop: Аниме",
        "categories": categories,
    }
    return render(request, 'base_delete_soon/anime_category.html', context=data)


def anime_category_products_view(request, category_slug):
    chosen_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=chosen_category)
    for product in products:
        # Получаем первую картинку для продукта
        first_image = product.images.first()
        if first_image:
            # Обновляем атрибут src для каждого продукта
            product.image_src = first_image.image.url
        else:
            # Если у продукта нет изображений, устанавливаем путь к заглушке
            product.image_src = static("base_delete_soon/images/cards/anime_category/sasuke.jpg")

    data = {
        "title": category_slug,
        "products": products,

    }
    return render(request, 'base_delete_soon/product_card.html', context=data)


def anime_products_view(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)

    data = {
        "title": product_slug,
        "product": product,
        "product_images": product_images,

    }
    return render(request, 'base_delete_soon/product.html', context=data)


def estetic_category_view(request):
    products = Product.objects.filter(category=3)
    for product in products:
        # Получаем первую картинку для продукта
        first_image = product.images.first()
        if first_image:
            # Обновляем атрибут src для каждого продукта
            product.image_src = first_image.image.url
        else:
            # Если у продукта нет изображений, устанавливаем путь к заглушке
            product.image_src = static("base_delete_soon/images/cards/anime_category/sasuke.jpg")

    data = {
        "title": "AniShop: Эстетика",
        "products": products,

    }
    return render(request, 'base_delete_soon/product_card.html', context=data)


def estetic_products_view(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)

    data = {
        "title": product_slug,
        "product": product,
        "product_images": product_images,
    }
    return render(request, 'base_delete_soon/product.html', context=data)


def base_view(request):
    data = {
        "title": "AniShop",
    }
    return render(request, 'index.html', context=data)
