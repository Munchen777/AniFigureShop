import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from products.models import Product
from roulette.models import SpinAttempt


# Create your views here.
def random_category_view(request: HttpRequest):
    # Находим пользователя
    user = request.user
    products = Product.objects.filter(category=2)

    # Если пользователь найден, то перенаправляем на страницу login
    if user.is_anonymous:
        return redirect('users:login')

    spin_attempt, created = SpinAttempt.objects.get_or_create(user=user)
    data = {
        "title": "AniShop: Рандом",
        "products": products,
        'attempts': spin_attempt.attempts,
    }
    return render(request, 'base_delete_soon/random_category.html', context=data)


def save_roulette_bonus(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        # Получаем или создаём запись для пользователя
        spin_attempt, created = SpinAttempt.objects.get_or_create(user=request.user)
        print(spin_attempt.attempts)
        # Проверяем, есть ли у пользователя доступные попытки
        if spin_attempt.attempts > 0:
            # Уменьшаем количество попыток на 1
            spin_attempt.attempts -= 1
            spin_attempt.save()

            # Логика определения выигрыша
            prize = data["name"]  # Приз, полученный через JS
            print(data)
            print(prize)

            # Возвращаем приз в ответе
            return render(request, 'base_delete_soon/random_category.html')
        else:
            return JsonResponse({'status': 'No spin attempts left'}, status=400)

    return JsonResponse({'status': 'Invalid request'}, status=400)



def bonuses_page_view(request):
    return render(request, 'base_delete_soon/bonuses_page.html')


def promotion_page_view(request):
    return render(request, 'base_delete_soon/bonuses_page.html')

