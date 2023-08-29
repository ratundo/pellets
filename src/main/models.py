from django.db import models


# Create your models here.
class CurrencyRates(models.Model):
    pair_name = models.CharField(max_length=10, blank=False)
    rate = models.FloatField()

    def __str__(self):
        return f"{self.rate}"


class HappyCustomers(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    company_link = models.URLField()
    company_logo = models.ImageField(upload_to="static/logos/", null=True, blank=True)


class Options(models.Model):
    marge = models.FloatField()
    delta_for_offer_update = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return "Options"


class Checkpoints(models.Model):
    checkpoint_location = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=150)

    def __str__(self):
        return str(self.checkpoint_location)


class Countries(models.Model):
    country_region = models.CharField(max_length=50)
    checkpoints = models.ManyToManyField(Checkpoints, blank=True)
    rate_eur_per_km = models.FloatField()
    minimal_rate = models.IntegerField()
    additional_expences = models.IntegerField()

    def __str__(self):
        return str(self.country_region)


class Languages(models.Model):
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.language_name)
