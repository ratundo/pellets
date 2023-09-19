from django.shortcuts import render  # NOQA
from django.views.generic import ListView

from main.models import HappyCustomers


# Create your views here.
class HappyCustomerView(ListView):
    model = HappyCustomers
    template_name = "index.html"
    context_object_name = "happy_customers"
