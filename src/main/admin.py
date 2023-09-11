from django.contrib import admin

from main.forms import CountriesForm
from main.models import (Checkpoints, Countries, CurrencyRates, HappyCustomers,
                         Languages, Options)

# Register your models here.
admin.site.register([CurrencyRates, HappyCustomers, Options, Checkpoints, Languages])


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    form = CountriesForm
