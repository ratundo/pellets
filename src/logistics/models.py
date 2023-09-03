import requests
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from goods.models import Factory
from inquiry.models import Inquiry
from logistics.gm_api_key import API_KEY
from main.models import Countries
#from offer.models import PrimaryOffer


# Create your models here.


class DistanceCalculator(models.Model):
    start_point = models.ForeignKey(Factory, on_delete=models.CASCADE, unique=False)
    checkpoints = models.ManyToManyField(Countries, blank=True)
    end_point = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=8, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_point.location} - {self.end_point.place_of_delivery} {self.end_point.zip_code}"

    class Meta:
        unique_together = ["start_point", "end_point", "zip_code"]

    @staticmethod
    def calculate_distance(start_point, intermediate_point, end_point, api_key):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"

        params = {
            "units": "metric",
            "origins": start_point,
            "waypoints": intermediate_point,
            "destinations": end_point,
            "key": api_key,
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data["status"] == "OK":
            try:
                distance_in_meters = data["rows"][0]["elements"][0]["distance"]["value"]
                distance_in_kilometers = distance_in_meters / 1000
                rounded_distance = round(distance_in_kilometers)
                return rounded_distance
            except KeyError:
                return 0
        else:
            return 0

    def clean(self):
        existing_distance = (
            DistanceCalculator.objects.filter(start_point=self.start_point, end_point=self.end_point)
            .exclude(pk=self.pk)
            .exists()
        )

        if existing_distance:
            raise ValidationError("A distance calculation with this Start point and End point already exists.")

    def save(self, *args, **kwargs):
        existing_distance = (
            DistanceCalculator.objects.filter(start_point=self.start_point, end_point=self.end_point)
            .exclude(pk=self.pk)
            .exists()
        )
        if existing_distance:
            return
        if self.start_point and self.end_point and (not self.distance or self.distance == 0):
            api_key = API_KEY
            origin = self.start_point.location
            destination = f"{self.end_point.place_of_delivery} {self.end_point.zip_code}"
            checkpoints = self.end_point.country.checkpoints.all()

            distances = []
            for checkpoint in checkpoints:
                waypoints = f"{checkpoint.coordinates}"
                distance = self.calculate_distance(origin, waypoints, destination, api_key)
                distances.append(distance)

            self.distance = min(distances)

        super().save(*args, **kwargs)






# class PrimaryOffer(models.Model):
#     inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name="offers")
#     factory = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)
#     distance = models.ForeignKey(
#         DistanceCalculator, on_delete=models.CASCADE, related_name="offer_distances", blank=True
#     )
#     marge = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="offer_marges")
#     product = models.ForeignKey(Goods, on_delete=models.CASCADE, blank=True, null=True)
#     price_fca = models.FloatField(blank=True, null=True)
#     tonnage = models.FloatField(blank=True, null=True)
#     delivery_price = models.FloatField(blank=True, null=True)
#     price_dap = models.FloatField(blank=True, null=True)
#     photos = models.URLField(null=True, blank=True)

