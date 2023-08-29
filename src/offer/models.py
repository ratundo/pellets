from django.db import models

from goods.models import Factory, Goods
from inquiry.models import Inquiry
from logistics.models import DistanceCalculator
from main.models import Options


class PrimaryOffer(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name="offers")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)
    distance = models.ForeignKey(
        DistanceCalculator, on_delete=models.CASCADE, related_name="offer_distances", blank=True
    )
    marge = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="offer_marges")
    product = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=True, null=True)
    price_fca = models.FloatField(blank=True, null=True)
    tonnage = models.FloatField(blank=True, null=True)
    delivery_price = models.FloatField(blank=True, null=True)
    price_dap = models.FloatField(blank=True, null=True)
    photos = models.URLField(null=True, blank=True)


class UpdatedOffer(models.Model):
    primary_offer = models.ForeignKey(PrimaryOffer, related_name="updated_offers", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name="updated_offers", on_delete=models.CASCADE)
    old_price = models.FloatField()
    new_price = models.FloatField()
    delta_for_offer_update = models.ForeignKey(Options, related_name="updated_offers", on_delete=models.CASCADE)
    change_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        ...
        super().save(*args, **kwargs)
