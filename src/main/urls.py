from django.urls import path

from main.views import HappyCustomerView

app_name = "main"  # NOQA

urlpatterns = [
    path("", HappyCustomerView.as_view(), name="happy_customers"),
]
