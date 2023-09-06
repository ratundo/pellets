from django.urls import include, path
from rest_framework import routers

from api.views import (CurrencyRateUpdateView, CustomerListCreateView,
                       DistanceDeleteView, DistanceListAPIView,
                       FactoryListCreateView, FactoryPriceUpdateView,
                       InquiryListCreateView, PrimaryOfferDeactivatorView,
                       PrimaryOfferListAPIView)

app_name = "api"
router = routers.DefaultRouter()
# router.register("rates", CurrencyRateUpdateView)

urlpatterns = [
    path("", include(router.urls)),
    path("rate/<int:pk>", CurrencyRateUpdateView.as_view(), name="currency_rate"),
    path("customers/", CustomerListCreateView.as_view(), name="customers"),
    path("factories/", FactoryListCreateView.as_view(), name="factories"),
    path("factories/<int:pk>", FactoryPriceUpdateView.as_view(), name="factory_price"),
    path("distance/", DistanceListAPIView.as_view(), name="distance_list"),
    path("distance/<int:pk>", DistanceDeleteView.as_view(), name="distance_delete"),
    path("inquiries/", InquiryListCreateView.as_view(), name="inquiries"),
    path("offers/", PrimaryOfferListAPIView.as_view(), name="offers"),
    path("offers/<int:pk>", PrimaryOfferDeactivatorView.as_view(), name="primary_offer_deactivator"),
]
