from django.contrib import admin
from .models import Tour, TourCategory

@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'departure_time', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
