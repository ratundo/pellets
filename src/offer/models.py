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
        DistanceCalculator, on_delete=models.CASCADE, related_name="offer_distances", blank=True, null=True
    )
    marge = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="offer_marges")
    product = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=True, null=True)
    price_fca = models.FloatField(blank=True, null=True)
    tonnage = models.FloatField(blank=True, null=True)
    delivery_price = models.FloatField(blank=True, null=True)
    price_dap = models.FloatField(blank=True, null=True)
    photos = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.inquiry.order_date} - {self.product} to {self.inquiry.place_of_delivery} for {self.inquiry.customer.company}"


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
    if action == "post_add":
        goods_ids = [good.pk for good in instance.goods.all()]
        factories = Factory.objects.filter(goods__in=goods_ids, active=True)
        zip_code = instance.zip_code

        for factory in factories:
            distance = DistanceCalculator.objects.filter(
                start_point=factory,
                zip_code=zip_code,
            ).first()

            if not distance:
                print("distance not exists")
                distance = DistanceCalculator.objects.create(
                    start_point=factory,
                    end_point=instance,
                    zip_code=zip_code,
                )
                distance.checkpoints.set([instance.country])
                distance_id = distance.id
            else:
                distance_id = distance.id

            print(f"distance: {distance_id}, factory: {factory}")

            # Creating offer

            factory_fca = factory.price_per_ton_eur
            marge = Options.objects.get(id=1).marge
            price_fca = factory_fca + (factory_fca * marge)
            price_fca = math.ceil(price_fca / 5) * 5
            tonnage = factory.goods.total_weight
            country = instance.country
            rate_eur_per_km = country.rate_eur_per_km
            add_expenses = country.additional_expences
            distance_calculated = DistanceCalculator.objects.get(id=distance_id).distance

            if distance_calculated != 0:
                delivery_price = (distance_calculated * rate_eur_per_km) + add_expenses
                delivery_price = math.ceil(delivery_price / 50) * 50
                price_dap = ((price_fca * tonnage) + delivery_price) / tonnage
                price_dap = round(price_dap, 2)
            else:
                delivery_price = None
                price_dap = None

            print(f"delivery_price: {delivery_price}")

            offer = PrimaryOffer.objects.create(
                inquiry=instance,
                factory=factory,
                distance=distance,
                marge=Options.objects.get(id=1),
                product=factory.goods,
                price_fca=price_fca,
                tonnage=tonnage,
                delivery_price=delivery_price,
                price_dap=price_dap,
            )
