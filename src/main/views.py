from django.shortcuts import render # NOQA
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]
    extra_context = {"site_name": "Super puper LMS", "description": "Sator arepo tenet opera rotas"}
