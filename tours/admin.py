from django.contrib import admin
from .models import HomeConfig, Section, SectionCard

class SectionCardInline(admin.TabularInline):
    model = SectionCard
    extra = 1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("home", "title", "layout", "columns", "max_items", "order", "is_active")
    list_filter = ("home__site", "home__channel", "layout", "is_active")
    search_fields = ("title", "subtitle", "slug")
    inlines = [SectionCardInline]
    fieldsets = (
        ("基本", {"fields": ("home", "title", "subtitle", "slug", "order", "is_active")}),
        ("版型", {"fields": ("layout", "columns", "show_divider", "max_items")}),
        ("更多連結", {"fields": ("more_label", "more_url")}),
    )

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    show_change_link = True
    fields = ("title","subtitle","slug","layout","columns","show_divider","max_items","more_label","more_url","order","is_active")

@admin.register(HomeConfig)
class HomeConfigAdmin(admin.ModelAdmin):
    list_display = ("site", "channel", "hero_title", "updated_at")
    list_filter = ("site", "channel")
    search_fields = ("hero_title", "seo_title")
    fieldsets = (
        ("站台/渠道", {"fields": ("site", "channel")}),
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "hero_bg_image", "show_breadcrumbs")}),
        ("SEO", {"fields": ("seo_title", "seo_description", "seo_keywords")}),
        ("登入後控制面板", {"fields": ("show_orders_widget","show_points_widget","show_profile_widget","show_coupons_widget")}),
        ("系統", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")
    inlines = []  # 區塊改由 SectionAdmin 獨立管理，避免太長
