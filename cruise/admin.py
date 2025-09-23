from django.contrib import admin
from .models import Region, CruisePort, CruiseTour


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name_zh_hant", "name_zh_hans", "name_en")
    search_fields = ("name_zh_hant", "name_zh_hans", "name_en")


@admin.register(CruisePort)
class CruisePortAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "name_zh_hant", "name_zh_hans", "name_en")
    list_filter = ("region",)
    search_fields = ("name_zh_hant", "name_zh_hans", "name_en")


@admin.register(CruiseTour)
class CruiseTourAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title_zh_hant",
        "title_zh_hans",
        "title_en",
        "departure_region",
        "departure_port",
        "departure_date",
        "price",
        "is_active",
    )
    list_filter = ("departure_region", "departure_port", "is_active")
    search_fields = ("title_zh_hant", "title_zh_hans", "title_en")
