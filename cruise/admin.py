from django.contrib import admin
from .models import CruiseTour, CruiseRegion, CruisePort


@admin.register(CruiseTour)
class CruiseTourAdmin(admin.ModelAdmin):
    list_display = (
        "title", "line", "region",
        "departure_port", "return_port",
        "departure_date", "price", "is_featured", "is_active"
    )
    list_filter = ("line", "region", "departure_port", "return_port", "is_featured", "is_active")
    search_fields = ("title", "line")


# 額外：也註冊 CruiseRegion & CruisePort 方便管理
@admin.register(CruiseRegion)
class CruiseRegionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(CruisePort)
class CruisePortAdmin(admin.ModelAdmin):
    list_display = ("name", "region")
    list_filter = ("region",)
    search_fields = ("name",)
