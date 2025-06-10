from django.contrib import admin
from .models import TourCategory, Tour

@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_zh_tw", "name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("title_zh_tw", "title_en", "category", "price", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title_zh_tw", "title_en")
