import json


from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpRequest
from django.templatetags.static import static
from django.views.generic import CreateView, DetailView, View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError

# from .forms import CreateOrderForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

# from carts.models import Cart, OrderItem, Order



def page_not_found(request, exception):
    return HttpResponseNotFound("Ne naidena brat")


# def anime_category_view(request):
#     categories = Category.objects.filter(parent_category=1)
#     print(categories)
#     data = {
#         "title": "AniShop: Аниме",
#         "categories": categories,
#     }
#     return render(request, 'base/anime_category.html', context=data)


# def anime_category_products_view(request, category_slug):
#     chosen_category = Category.objects.get(slug=category_slug)
#     products = Product.objects.filter(category=chosen_category)
#     for product in products:
#         # Получаем первую картинку для продукта
#         first_image = product.images.first()
#         if first_image:
#             # Обновляем атрибут src для каждого продукта
#             product.image_src = first_image.image.url
#         else:
#             # Если у продукта нет изображений, устанавливаем путь к заглушке
#             product.image_src = static("base/images/cards/anime_category/sasuke.jpg")

#     data = {
#         "title": category_slug,
#         "products": products,

#     }
#     return render(request, 'base/product_card.html', context=data)


# def anime_products_view(request, category_slug, product_slug):
#     product = Product.objects.get(slug=product_slug)
#     product_images = ProductImage.objects.filter(product=product)

#     data = {
#         "title": product_slug,
#         "product": product,
#         "product_images": product_images,

#     }
#     return render(request, 'base/product.html', context=data)


# def random_category_view(request):
#     products = Product.objects.filter(category=2)

#     data = {
#         "title": "AniShop: Рандом",
#         "products": products,
#     }
#     return render(request, 'base/random_category.html', context=data)


# def estetic_category_view(request):
#     products = Product.objects.filter(category=3)
#     for product in products:
#         # Получаем первую картинку для продукта
#         first_image = product.images.first()
#         if first_image:
#             # Обновляем атрибут src для каждого продукта
#             product.image_src = first_image.image.url
#         else:
#             # Если у продукта нет изображений, устанавливаем путь к заглушке
#             product.image_src = static("base/images/cards/anime_category/sasuke.jpg")

#     data = {
#         "title": "AniShop: Эстетика",
#         "products": products,

#     }
#     return render(request, 'base/product_card.html', context=data)


# def estetic_products_view(request, category_slug, product_slug):
#     product = Product.objects.get(slug=product_slug)
#     product_images = ProductImage.objects.filter(product=product)

#     data = {
#         "title": product_slug,
#         "product": product,
#         "product_images": product_images,
#     }
#     return render(request, 'base/product.html', context=data)


def base_view(request):
    data = {
        "title": "AniShop",
    }
    return render(request, 'index.html', context=data)


# def add_to_cart(request, product_id):
#     if request.user.is_authenticated:
#         user = request.user
#         product = Product.objects.get(id=product_id)

#         # Создаем запись в корзине
#         cart_item = Cart.add_to_cart(user=user, product=product, quantity=1)

#     return redirect('users:cart')


# def save_roulette_bonus(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         # Тут можно сохранить данные в базу данных, используя Django ORM
#         # Например:
#         # Модель.objects.create(field=data)
#         print(data)
#         return JsonResponse({'status': 'Data saved successfully'})
#     return JsonResponse({'status': 'Invalid request'}, status=400)


# @login_required
# def create_order(request: HttpRequest):
#     if request.method == "POST":
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 print(form.cleaned_data)
#                 user = request.user
#                 cart_items = Cart.objects.filter(user=user)
#                 if cart_items.exists():
#                     # Создаем заказ
#                     order = Order.objects.create(
#                         user=user,
#                         phone_number=form.cleaned_data['phone_number'],
#                         # requires_delivery=form.cleaned_data["requires_delivery"],
#                         delivery_address=form.cleaned_data["delivery_address"],
#                         promocode=form.cleaned_data["promocode"]
#                     )
                    
#                     # Создаем заказанные товары
#                     for cart_item in cart_items:
#                         product = cart_item.product
#                         name = cart_item.product.name
#                         price = cart_item.product.sell_price()
#                         quantity = cart_item.quantity
                        
#                         if product.quantity < quantity or not product.available:
#                             raise ValidationError(f"Недостаточное кол-во товара {name} на складе\nВ наличии: {product.quantity}")
                        
#                         OrderItem.objects.create(
#                             order=order,
#                             product=product,
#                             name=name,
#                             price=price,
#                             quantity=quantity
#                         )
#                         product.quantity -= quantity
#                         product.save()

#                     print("Заказ оформлен")
#                     # Очищаем корзину пользователя после создания заказа
#                     cart_items.delete()
#                     return redirect("users:profile")

#             except ValidationError as exc:
#                 pass
#         else:
#             print("Форма не прошла валидацию")

#     else:
#         initial = {
#             "first_name": request.user.first_name,
#             "last_name": request.user.last_name
#         }
#         form = CreateOrderForm(initial=initial)

#     context = {
#         "form": form
#     }
#     return render(request, "base/create-order.html", context=context)


# def all_products_view(request: HttpRequest):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         products = data['']
#     if request.headers.get("X-Requested-With") == "XMLHttpRequest":
#         category = request.POST["category"]
#         products = Product.objects.filter(category=category)
#         return JsonResponse({"products": products})

#     categories = Category.objects.all()
#     products = Product.objects.filter(archived=False,
#                                       available=True).values_list()

#     all_products = Product.objects.filter(
#         archived=False,
#         available=True
#     ).values_list('name')
    
#     serialized_products = json.dumps(list(products), cls=DjangoJSONEncoder)
    
#     context = {
#         "products": products,
#         "categories": categories,
#         "serialized_products": serialized_products
#     }
#     return render(request, "base/products_page.html", context=context)


# def ajax_selected_products_view(request: HttpRequest, category_slug) -> JsonResponse:
#     print(category_slug)
#     products = Product.objects.filter(category=category_slug).values()
#     print(products)
#     serialized_products = json.dumps(list(products), cls=DjangoJSONEncoder)
#     return JsonResponse({"products": serialized_products})


# def ajax_all_products_view(request: HttpRequest) -> JsonResponse:
#     all_products = Product.objects.all()
#     serialized_products = json.dumps(list(all_products), cls=DjangoJSONEncoder)
#     return JsonResponse({"all_products": serialized_products})





# # class ProductView(APIView):
# #     def get(self, request):
# #         output = [
# #             {
# #                 'pk': product.pk,
# #                 'name': product.name,
# #                 'description': product.description,
# #                 'category': product.category,
# #                 'price': product.price,
# #                 'slug': product.slug,
# #                 'order': product.order,
# #                 'discount': product.discount,
# #                 'archived': product.archived,
# #                 'available': product.available,
# #                 'created_by': product.created_by,
# #                 'updated_at': product.updated_at,
# #                 'created_at': product.created_at,
# #                 'quantity': product.quantity
# #             }
# #             for product in Product.objects.all()
# #         ]
# #         return Response(output)

# #     def post(self, request: HttpRequest):
# #         serializer = ProductSerializer(data=request.data)
# #         if serialize.is_valid(raise_exception=True):
# #             serialize.save()
# #             return Response(serializer.data)
