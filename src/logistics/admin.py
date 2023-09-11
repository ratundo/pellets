from django.contrib import admin

from logistics.models import DistanceCalculator


@admin.register(DistanceCalculator)
class DistanceCalculatorModelAdmin(admin.ModelAdmin):
    readonly_fields = ("start_point", "checkpoints", "end_point", "zip_code", "distance")
