from django.shortcuts import render # NOQA
from django.views.generic import ListView

from content.models import Faq


# Create your views here.
class FaqView(ListView):
    model = Faq
    template_name = "faq.html"
    context_object_name = "faq"
