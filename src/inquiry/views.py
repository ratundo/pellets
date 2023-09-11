from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from inquiry.forms import CombinedInquiryForm
from inquiry.models import Inquiry


class CombinedInquiryCreateView(CreateView):
    model = Inquiry
    form_class = CombinedInquiryForm
    template_name = "inquiry.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, "Inquiry sent successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})
