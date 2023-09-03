from django import forms
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.formfields import PhoneNumberField

from goods.models import Goods
from inquiry.models import Customer, Inquiry
from inquiry.utils.validators import validate_customer_name
from main.models import Countries, Languages


class CombinedInquiryForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=150, validators=[validate_customer_name])
    company = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = PhoneNumberField(max_length=16)
    language = forms.ModelChoiceField(queryset=Languages.objects.all(), empty_label="Select a language")
    country = forms.ModelChoiceField(queryset=Countries.objects.all(), empty_label="Select a country")

    place_of_delivery = forms.CharField(max_length=150)
    zip_code = forms.CharField(max_length=8)

    goods = forms.ModelMultipleChoiceField(queryset=Goods.objects.all(), required=False)

    class Meta:
        model = Inquiry
        fields = [
            "customer_name",
            "company",
            "email",
            "phone_number",
            "language",
            "place_of_delivery",
            "zip_code",
            "country",
            "goods",
        ]

    def save(self, commit=True):
        email = self.cleaned_data['email']

        try:
            customer = Customer.objects.get(email=email)
        except ObjectDoesNotExist:

            customer = Customer.objects.create(
                name=self.cleaned_data['customer_name'],
                company=self.cleaned_data['company'],
                email=email,
                phone_number=self.cleaned_data['phone_number'],
                language=self.cleaned_data['language']
            )


        inquiry = Inquiry.objects.create(
            customer=customer,
            place_of_delivery=self.cleaned_data['place_of_delivery'],
            zip_code=self.cleaned_data['zip_code'],
            country=self.cleaned_data['country']
        )
        inquiry.goods.set(self.cleaned_data['goods'])

        return inquiry
