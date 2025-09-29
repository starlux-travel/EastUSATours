from django.contrib import admin
from tours.models import DepartureRegion, DepartureCity, Tour
from cruise.models import CruiseRegion, CruisePort, CruiseTour, Banner


# ========== Tours ==========
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
    list_display = ("id", "title_zh_tw", "title_zh_cn", "title_en", "is_featured")
    search_fields = ("title_zh_tw", "title_zh_cn", "title_en")
    list_filter = ("is_featured", "departure_city", "departure_region")


# ========== Cruise ==========
@admin.register(CruiseRegion)
class CruiseRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(CruisePort)
class CruisePortAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    list_filter = ("region",)
    search_fields = ("name", "region__name")


@admin.register(CruiseTour)
class CruiseTourAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title_zh_tw",
        "title_zh_cn",
        "title_en",
        "departure_region",
        "departure_port",
        "departure_date",
        "price",
        "is_active",
    )
    list_filter = ("departure_region", "departure_port", "is_active")
    search_fields = ("title_zh_tw", "title_zh_cn", "title_en")


# ========== Banner ==========
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)
    ordering = ("order",)
