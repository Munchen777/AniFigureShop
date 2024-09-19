from django.shortcuts import render, redirect

from products.models import Product
from users.models import CartItem


# Create your views here.
def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(id=product_id)

        # Создаем запись в корзине
        cart_item = CartItem.add_to_cart(user=user, product=product, quantity=quantity)

    return redirect('users:cart')


