from django.urls import path

from content.views import FaqView

app_name = "content"  # NOQA

urlpatterns = [
    path("faq/", FaqView.as_view(), name="faq"),
]
