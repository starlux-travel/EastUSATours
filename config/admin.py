from django.contrib import admin
from .models import SiteTheme

@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'updated_at')
