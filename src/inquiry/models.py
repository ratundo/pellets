from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from goods.models import Goods
from main.models import Countries, Languages


class Customer(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(_("phone number"), max_length=16)
    language = models.ForeignKey(Languages, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company)


class Inquiry(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, blank=True, null=True)
    place_of_delivery = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=8)
    goods = models.ManyToManyField(Goods, blank=True)

    def __str__(self):
        formatted_date = self.order_date.strftime("%Y-%m-%d %H:%M:%S")
        goods_list = ", ".join(str(good) for good in self.goods.all())
        return f"{formatted_date} {self.place_of_delivery} Goods: {goods_list} - Country: {self.country} Customer: {self.customer}"

    class Meta:
        get_latest_by = "order_date"
