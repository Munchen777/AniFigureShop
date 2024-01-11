from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound


def page_not_found(request, exception):
    return HttpResponseNotFound("Ne naidena brat")


def main_page(request):
    return HttpResponse("THIS IS A MAIN PAGE")


def base_view(request):
    data = {
        "title": "ШАБЛОН ГЛАВНОЙ СТРАНИЦЫ",
    }
    return render(request, 'base/base.html', context=data)
