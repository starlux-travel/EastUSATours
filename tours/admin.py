# tours/admin.py
from django.contrib import admin
from .models import HomeConfig, Section, SectionCard

class SectionCardInline(admin.TabularInline):
    model = SectionCard
    extra = 1
    fields = ("title", "subtitle", "image_url", "price_label", "tag", "link_url", "order", "is_active")
    ordering = ("order", "id",)

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    fields = (
        "title", "subtitle", "slug", "layout", "columns",
        "show_divider", "max_items", "more_label", "more_url",
        "order", "is_active",
    )
    ordering = ("order", "id",)
    show_change_link = True

    inlines = [SectionCardInline]  # Django 不支援 inline 的 inline（僅顯示一層）
    # 小撇步：在 Section 頁面再編卡片

@admin.register(HomeConfig)
class HomeConfigAdmin(admin.ModelAdmin):
    list_display = ("site", "channel", "hero_title", "updated_at")
    list_filter = ("site", "channel")
    search_fields = ("hero_title", "seo_title")
    inlines = [SectionInline]
    fieldsets = (
        ("基本", {"fields": ("site", "channel")}),
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "hero_bg_image", "show_breadcrumbs")}),
        ("SEO", {"fields": ("seo_title", "seo_description", "seo_keywords")}),
        ("會員小工具", {
            "fields": ("show_orders_widget", "show_points_widget", "show_profile_widget", "show_coupons_widget")
        }),
    )

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "home", "layout", "columns", "order", "is_active")
    list_filter = ("home__site", "home__channel", "layout", "is_active")
    search_fields = ("title", "subtitle", "slug")
    ordering = ("home", "order", "id")

@admin.register(SectionCard)
class SectionCardAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "tag", "price_label", "order", "is_active")
    list_filter = ("section__home__site", "section__home__channel", "is_active")
    search_fields = ("title", "subtitle", "tag")
    ordering = ("section", "order", "id")
