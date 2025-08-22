# tours/serializers.py
from rest_framework import serializers
from .models import HomeConfig, Section, SectionCard

class SectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCard
        fields = (
            "title", "subtitle", "image_url",
            "price_label", "tag", "link_url",
            "order", "is_active",
        )

class SectionSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = (
            "title", "subtitle", "slug",
            "layout", "columns", "show_divider",
            "max_items", "more_label", "more_url",
            "order", "is_active", "cards",
        )

    def get_cards(self, obj: Section):
        qs = obj.cards.filter(is_active=True).order_by("order", "id")
        if obj.max_items:
            qs = qs[:obj.max_items]
        return SectionCardSerializer(qs, many=True).data

class HomePayloadSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = HomeConfig
        fields = (
            "hero_title", "hero_subtitle", "hero_bg_image", "show_breadcrumbs",
            "seo_title", "seo_description", "seo_keywords",
            "sections", "updated_at",
        )
