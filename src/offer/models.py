import math


from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from goods.models import Factory, Goods
from inquiry.models import Inquiry
from logistics.models import DistanceCalculator
from main.models import Options


class PrimaryOffer(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name="offers")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)
    distance = models.ForeignKey(
        DistanceCalculator, on_delete=models.CASCADE, related_name="offer_distances", blank=True, null=True)
    marge = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="offer_marges")
    product = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=True, null=True)
    price_fca = models.FloatField(blank=True, null=True)
    tonnage = models.FloatField(blank=True, null=True)
    delivery_price = models.FloatField(blank=True, null=True)
    price_dap = models.FloatField(blank=True, null=True)
    photos = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        factory_fca = self.factory.price_per_ton_eur
        self.price_fca = factory_fca + (factory_fca * self.marge.marge)
        self.price_fca = math.ceil(self.price_fca / 5) * 5
        self.tonnage = self.product.total_weight
        country = self.inquiry.country
        rate_eur_per_km = self.distance.checkpoints.get(country_region=country).rate_eur_per_km
        add_expences = self.distance.checkpoints.get(country_region=country).additional_expences
        self.delivery_price = (self.distance.distance * rate_eur_per_km) + add_expences
        self.delivery_price = math.ceil(self.delivery_price / 50) * 50
        self.price_dap = ((self.price_fca * self.tonnage) + self.delivery_price) / self.tonnage
        self.price_dap = round(self.price_dap, 2)

        super().save(*args, **kwargs)


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


@receiver(m2m_changed, sender=Inquiry.goods.through)
def inquiry_goods_changed(sender, instance, action, **kwargs):
    if action == 'post_add':
        goods_ids = [good.pk for good in instance.goods.all()]
        factories = Factory.objects.filter(goods__in=goods_ids, active=True)
        zip_code = instance.zip_code

        for factory in factories:
            existing_distance = DistanceCalculator.objects.filter(
                start_point=factory,
                zip_code=zip_code,
            ).first()

            if not existing_distance:
                print("distance not exists")
                distance = DistanceCalculator.objects.create(
                    start_point=factory,
                    end_point=instance,
                    zip_code=zip_code,
                )
                distance.checkpoints.set([instance.country])
                distance_id = distance.id
            else:
                distance_id = existing_distance.id

            print(f"distance: {distance_id}, factory: {factory}")

            # Creating offer

            offer = PrimaryOffer.objects.create(
                inquiry=instance,
                factory=factory,
                distance=existing_distance,
                marge=Options.objects.get(id=1),
                product=factory.goods,
            )