from django.contrib import admin
from .models import Tour, DepartureRegion, DepartureCity


@admin.register(DepartureRegion)
class DepartureRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(DepartureCity)
class DepartureCityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    list_filter = ("region",)
    search_fields = ("name", "region__name")


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "departure_date", "departure_city", "views_count")
    list_filter = ("departure_city", "departure_date")
    search_fields = ("title", "description")
