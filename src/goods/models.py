from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import CurrencyRates


# Create your models here.
class Goods(models.Model):
    product_name = models.CharField(max_length=50)
    total_weight = models.DecimalField(max_digits=4, decimal_places=2)
    package = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_name} {self.package}"


class Factory(models.Model):
    goods = models.ForeignKey(Goods, blank=True, default=1, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, unique=False)
    pseudo_name = models.CharField(max_length=50)
    price_per_ton_uah = models.SmallIntegerField(null=True, blank=True)
    uah_eur_rate = models.ForeignKey(CurrencyRates, on_delete=models.CASCADE)
    price_per_ton_eur = models.SmallIntegerField(null=True, blank=True)
    product_photos = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True, db_column='Active')

    def __str__(self):
        return f"{self.location} {self.goods}"

    def save(self, *args, **kwargs):
        if not self.price_per_ton_eur and self.price_per_ton_uah and self.uah_eur_rate:
            exchange_rate = self.uah_eur_rate.rate
            self.price_per_ton_eur = self.price_per_ton_uah / exchange_rate
        super().save(*args, **kwargs)


@receiver(post_save, sender=CurrencyRates)
def update_factory_prices(sender, instance, **kwargs):
    exchange_rate = instance.rate
    factories = Factory.objects.filter(uah_eur_rate=instance)

    for factory in factories:
        if factory.price_per_ton_uah:
            factory.price_per_ton_eur = factory.price_per_ton_uah / exchange_rate
            factory.save()
