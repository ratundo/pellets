from decouple import config
from django.core.exceptions import ValidationError
from django.test import TestCase

from goods.models import Factory, Goods
from inquiry.models import Customer, Inquiry
from logistics.models import DistanceCalculator
from main.models import (Checkpoints, Countries, CurrencyRates, Languages,
                         Options)


class DistanceCalculatorTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.currency_rate = CurrencyRates.objects.create(
            pair_name="EURUAH",
            rate=40.01,
        )

    def setUp(self):
        self.goods = Goods.objects.create(product_name="Product", total_weight=22.77, package="Package")

        self.uah_eur_rate = CurrencyRates.objects.create(
            pair_name="EURUAH",
            rate=40.01,
        )
        self.options = Options.objects.create(
            marge=0.1,
            delta_for_offer_update=5,
        )
        self.factory = Factory.objects.create(
            location="Lviv", pseudo_name="Lviv", price_per_ton_uah=100, uah_eur_rate=self.currency_rate
        )
        self.country = Countries.objects.create(
            country_region="Czech Republic",
            rate_eur_per_km=0.1,
            minimal_rate=850,
            additional_expences=0,
        )
        self.checkpoint_1 = Checkpoints.objects.create(
            checkpoint_location="Uzhgorod/Vysne-Nemecke",
            coordinates="48.65439077268193, 22.265290199729403",
        )
        self.checkpoint_2 = Checkpoints.objects.create(
            checkpoint_location="Krakivets/Korczowa",
            coordinates="49.9549853055345, 23.114746637072994",
        )
        self.country.checkpoints.add(self.checkpoint_1, self.checkpoint_2)

        self.languages = Languages.objects.create(language_name="English")

        self.customer = Customer.objects.create(
            name="John Doe",
            company="Camomile",
            email="example@example.com",
            phone_number="+380502113366",
            language=self.languages,
        )

        self.inquiry = Inquiry.objects.create(
            place_of_delivery="Kolin",
            zip_code="280 02",
            country=self.country,
            customer=self.customer,
        )

    def test_delivery_checkpoint(self):
        distance_calculator = DistanceCalculator.objects.create(  # NOQA
            start_point=self.factory,
            end_point=self.inquiry,
        )

        checkpoints = self.inquiry.country.checkpoints.all()

        min_distance = float("inf")
        closest_checkpoint = None

        for checkpoint in checkpoints:
            intermediate_point = checkpoint.coordinates
            calculated_distance = DistanceCalculator.calculate_distance(
                self.factory.location,
                intermediate_point,
                f"{self.inquiry.place_of_delivery} {self.inquiry.zip_code}",
                config("GM_API_KEY"),
            )

            if calculated_distance < min_distance:
                min_distance = calculated_distance
                closest_checkpoint = checkpoint

        expected_checkpoint = self.checkpoint_1

        self.assertEqual(closest_checkpoint, expected_checkpoint)

    def test_unique_distance_calculator(self):
        distance_calculator1 = DistanceCalculator(
            start_point=self.factory,
            end_point=self.inquiry,
            distance=500,
        )
        distance_calculator1.save()

        distance_calculator2 = DistanceCalculator(
            start_point=self.factory,
            end_point=self.inquiry,
            distance=500,
        )

        with self.assertRaises(ValidationError):
            distance_calculator2.full_clean()

