from django.urls import path

from inquiry.views import CombinedInquiryCreateView

app_name = "inquiry"  # NOQA

urlpatterns = [
    path("", CombinedInquiryCreateView.as_view(), name="create_inquiry"),

]