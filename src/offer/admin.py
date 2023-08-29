from django.contrib import admin

from offer.models import PrimaryOffer, UpdatedOffer

# Register your models here.
admin.site.register([PrimaryOffer, UpdatedOffer])
