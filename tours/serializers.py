# tours/serializers.py
from rest_framework import serializers
from .models import Tour
from .utils import pick_lang

class TourSerializer(serializers.ModelSerializer):
    display_title = serializers.SerializerMethodField()
    display_desc = serializers.SerializerMethodField()
    display_faq = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = [
            "id", "tour_type",
            "title", "desc", "faq",
            "display_title", "display_desc", "display_faq",
            "meeting_point", "pickup_time",
            "embark_port", "sail_date", "cabin_type",
            "price", "cover_image", "is_active",
            "updated_at",
        ]

    def _lang(self):
        request = self.context.get("request")
        return (request.query_params.get("lang") if request else None) or "zh-Hant"

    def get_display_title(self, obj):
        return pick_lang(obj.title or {}, self._lang())

    def get_display_desc(self, obj):
        return pick_lang(obj.desc or {}, self._lang())

    def get_display_faq(self, obj):
        return pick_lang(obj.faq or {}, self._lang())
