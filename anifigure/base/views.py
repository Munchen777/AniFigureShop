from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.templatetags.static import static
from django.views.generic import CreateView

from base.models import Category, Product, ProductImage
from users.models import CartItem


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
    for product in products:
        # Получаем первую картинку для продукта
        first_image = product.images.first()
        if first_image:
            # Обновляем атрибут src для каждого продукта
            product.image_src = first_image.image.url
        else:
            # Если у продукта нет изображений, устанавливаем путь к заглушке
            product.image_src = static("base/images/cards/anime_category/sasuke.jpg")

    data = {
        "title": category_slug,
        "products": products,

    }
    return render(request, 'base/product_card.html', context=data)


def anime_products_view(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)

    data = {
        "title": product_slug,
        "product": product,
        "product_images": product_images,

    }
    return render(request, 'base/product.html', context=data)


def random_category_view(request):
    products = Product.objects.filter(category=2)

    data = {
        "title": "AniShop: Рандом",
        "products": products,
    }
    return render(request, 'base/random_category.html', context=data)


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
            product.image_src = static("base/images/cards/anime_category/sasuke.jpg")

    data = {
        "title": "AniShop: Эстетика",
        "products": products,

    }
    return render(request, 'base/product_card.html', context=data)


def estetic_products_view(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)

    data = {
        "title": product_slug,
        "product": product,
        "product_images": product_images,
    }
    return render(request, 'base/product.html', context=data)


def base_view(request):
    data = {
        "title": "AniShop",
    }
    return render(request, 'base/base.html', context=data)


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(id=product_id)

        # Создаем запись в корзине
        cart_item = CartItem(user=user, product=product, quantity=1)
        cart_item.save()

    return redirect('users:cart')
