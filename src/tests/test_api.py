from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient, APITestCase

from goods.models import Factory, Goods
from inquiry.models import Customer, Inquiry
from logistics.models import DistanceCalculator
from main.models import (Checkpoints, Countries, CurrencyRates, Languages,
                         Options)


class TestApi(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.currency_rate = CurrencyRates.objects.create(
            pair_name="EURUAH",
            rate=40.01,
        )

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(username="test_admin")
        self.user.set_password("qwerty1234")
        self.user.save()

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

    def test_avaliability(self):
        self.client.force_authenticate(user=self.user)
        apis = ["customers", "factories", "distance_list", "inquiries"]
        for api in apis:
            result = self.client.get(reverse(f"api:{api}"))
            self.assertEqual(result.status_code, HTTP_200_OK)
        print("all APIs are available")

    def test_unauthenticated_client(self):
        apis = ["customers", "factories", "distance_list", "inquiries"]
        for api in apis:
            result = self.client.get(reverse(f"api:{api}"))
            self.assertEqual(result.status_code, HTTPStatus.UNAUTHORIZED)
        print("all APIs are secured")

    def test_factory_update_price(self):
        self.client.force_authenticate(user=self.user)
        new_price_per_ton_uah = 150
        factory_update_data = {
            "price_per_ton_uah": new_price_per_ton_uah,
        }
        update_response = self.client.patch(reverse("api:factory_price", kwargs={"pk": 1}), factory_update_data)
        self.assertEqual(Factory.objects.get(id=1).price_per_ton_uah, new_price_per_ton_uah)

    def test_new_customer_create(self, create_response=None):
        self.client.force_authenticate(user=self.user)
        new_customer = {
            "name": "NewName",
            "company": "NewCompany",
            "email": "new_email@email.com",
            "phone_number": "+380992342323",
            "language": 1,
        }
        create_customer = self.client.post(reverse("api:customers"), new_customer)
        created_customer = Customer.objects.filter(name="NewName").first()

        self.assertEqual(create_customer.status_code, HTTPStatus.CREATED)
        self.assertIsNotNone(created_customer)

    def test_distance_delete(self):
        self.client.force_authenticate(user=self.user)

        distance_calculator = DistanceCalculator.objects.create(
            start_point=self.factory,
            end_point=self.inquiry,
            zip_code="12345",
            distance=100.0,
        )
        delete_url = reverse("api:distance_delete", kwargs={"pk": distance_calculator.pk})
        delete_response = self.client.delete(delete_url)

        self.assertEqual(delete_response.status_code, HTTPStatus.NO_CONTENT)
        self.assertIsNone(DistanceCalculator.objects.filter(pk=distance_calculator.pk).first())
