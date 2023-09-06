from rest_framework.serializers import ModelSerializer

from goods.models import Factory, Goods
from inquiry.models import Customer, Inquiry
from logistics.models import DistanceCalculator
from main.models import Countries, CurrencyRates
from offer.models import PrimaryOffer


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = ("rate",)


class GoodsSerializer(ModelSerializer):
    class Meta:
        model = Goods
        fields = ("product_name", "total_weight", "package")


class FactorySerializer(ModelSerializer):
    goods = GoodsSerializer()
    uah_eur_rate = CurrencyRateSerializer()

    class Meta:
        model = Factory
        fields = (
            "pk",
            "goods",
            "location",
            "pseudo_name",
            "price_per_ton_uah",
            "uah_eur_rate",
            "price_per_ton_eur",
            "active",
        )


class FactoryPriceSerializer(ModelSerializer):
    class Meta:
        model = Factory
        fields = ("pk", "goods", "location", "pseudo_name", "price_per_ton_uah", "price_per_ton_eur", "active")


class FactoryLocationSerializer(ModelSerializer):
    class Meta:
        model = Factory
        fields = ("location",)


class PlaceOfDeliverySerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("place_of_delivery",)


class CountryNameSerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = ("country_region",)


class DistanceCollectionSerializer(ModelSerializer):
    start_point = FactoryLocationSerializer()
    end_point = PlaceOfDeliverySerializer()

    class Meta:
        model = DistanceCalculator
        fields = ("pk", "start_point", "end_point", "zip_code", "distance")


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "company", "email", "phone_number", "language")


class InquirySerializer(ModelSerializer):
    customer = CustomerSerializer()
    country = CountryNameSerializer()
    goods = GoodsSerializer(many=True)

    class Meta:
        model = Inquiry
        fields = ("order_date", "customer", "country", "place_of_delivery", "zip_code", "goods")


class PrimaryOfferSerializer(ModelSerializer):
    inquiry = InquirySerializer()
    factory = FactorySerializer()

    class Meta:
        model = PrimaryOffer
        fields = ("pk", "inquiry", "factory", "price_fca", "delivery_price", "price_dap", "active")


class PrimaryOfferDeactivatorSerializer(ModelSerializer):
    class Meta:
        model = PrimaryOffer
        fields = ("active",)
