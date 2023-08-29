import requests
from django.core.exceptions import ValidationError
from django.db import models

from goods.models import Factory
from inquiry.models import Inquiry
from logistics.gm_api_key import API_KEY
from main.models import Countries

# Create your models here.


class DistanceCalculator(models.Model):
    start_point = models.ForeignKey(Factory, on_delete=models.CASCADE, unique=False)
    checkpoints = models.ManyToManyField(Countries, blank=True)
    end_point = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    distance = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_point.location} - {self.end_point.place_of_delivery} {self.end_point.zip_code}"

    class Meta:
        unique_together = ["start_point", "end_point"]

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
