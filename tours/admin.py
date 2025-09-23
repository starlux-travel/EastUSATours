from django.contrib import admin
from .models import DepartureRegion, DepartureCity, Tour


@admin.register(DepartureRegion)
class DepartureRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name_zh_hant", "name_zh_hans", "name_en")
    search_fields = ("name_zh_hant", "name_zh_hans", "name_en")


@admin.register(DepartureCity)
class DepartureCityAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "name_zh_hant", "name_zh_hans", "name_en")
    list_filter = ("region",)
    search_fields = ("name_zh_hant", "name_zh_hans", "name_en")


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title_zh_hant",
        "title_zh_hans",
        "title_en",
        "departure_region",
        "departure_city",
        "departure_date",
        "price",
        "is_active",
    )
    list_filter = ("departure_region", "departure_city", "is_active")
    search_fields = ("title_zh_hant", "title_zh_hans", "title_en")
