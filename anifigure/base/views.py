from django.views.generic import TemplateView
from django.http import HttpResponseNotFound


def page_not_found(request, exception):
    return HttpResponseNotFound("Ne naidena brat")


class IndexTemplateView(TemplateView):
    template_name = "index.html"
