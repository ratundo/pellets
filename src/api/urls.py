from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CurrencyRateUpdateView, CustomerListCreateView,
                       DistanceDeleteView, DistanceListAPIView,
                       FactoryListCreateView, FactoryPriceUpdateView,
                       InquiryListCreateView, PrimaryOfferDeactivatorView,
                       PrimaryOfferListAPIView)

app_name = "api"
router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Pellets API",
        default_version="v1",
        description="API for processing orders and price updates",
        term_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

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
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
]
