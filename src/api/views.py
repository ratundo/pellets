from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)

from api.serializers import (CurrencyRateSerializer, CustomerSerializer,
                             DistanceCollectionSerializer,
                             FactoryPriceSerializer, FactorySerializer,
                             InquirySerializer,
                             PrimaryOfferDeactivatorSerializer,
                             PrimaryOfferSerializer)
from goods.models import Factory
from inquiry.models import Customer, Inquiry
from logistics.models import DistanceCalculator
from main.models import CurrencyRates
from offer.models import PrimaryOffer


class CurrencyRateUpdateView(RetrieveUpdateAPIView):
    queryset = CurrencyRates.objects.filter(id=1).values("rate")
    serializer_class = CurrencyRateSerializer


class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FactoryListCreateView(ListCreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryPriceUpdateView(RetrieveUpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryPriceSerializer


class DistanceListAPIView(ListAPIView):
    queryset = DistanceCalculator.objects.all()
    serializer_class = DistanceCollectionSerializer


class DistanceDeleteView(RetrieveDestroyAPIView):
    queryset = DistanceCalculator.objects.all()
    serializer_class = DistanceCollectionSerializer


class InquiryListCreateView(ListCreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class PrimaryOfferListAPIView(ListAPIView):
    queryset = PrimaryOffer.objects.all()
    serializer_class = PrimaryOfferSerializer


class PrimaryOfferDeactivatorView(RetrieveUpdateAPIView):
    queryset = PrimaryOffer.objects.all()
    serializer_class = PrimaryOfferDeactivatorSerializer
