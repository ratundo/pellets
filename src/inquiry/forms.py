from django import forms

from main.models import Countries, Languages

from .models import Customer, Inquiry


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "company", "email", "phone_number", "language"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["language"].queryset = Languages.objects.all()


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["place_of_delivery", "zip_code", "goods", "country"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["country"].queryset = Countries.objects.all()
