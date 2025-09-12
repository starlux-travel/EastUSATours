from django.contrib import admin
from django import forms
from .models import Tour, TourType


class TourAdminForm(forms.ModelForm):
    # --- Title 三語 ---
    title_zh_Hant = forms.CharField(label="標題（繁）", required=False)
    title_zh_Hans = forms.CharField(label="標題（簡）", required=False)
    title_en = forms.CharField(label="Title (EN)", required=False)

    # --- Description 三語 ---
    desc_zh_Hant = forms.CharField(label="說明（繁）", required=False, widget=forms.Textarea)
    desc_zh_Hans = forms.CharField(label="說明（簡）", required=False, widget=forms.Textarea)
    desc_en = forms.CharField(label="Description (EN)", required=False, widget=forms.Textarea)

    # --- FAQ 三語 ---
    faq_zh_Hant = forms.CharField(label="FAQ（繁）", required=False, widget=forms.Textarea)
    faq_zh_Hans = forms.CharField(label="FAQ（簡）", required=False, widget=forms.Textarea)
    faq_en = forms.CharField(label="FAQ (EN)", required=False, widget=forms.Textarea)

    class Meta:
        model = Tour
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def prefill(block, prefix):
            d = (block or {})
            self.fields[f"{prefix}_zh_Hant"].initial = d.get("zh_Hant", "")
            self.fields[f"{prefix}_zh_Hans"].initial = d.get("zh_Hans", "")
            self.fields[f"{prefix}_en"].initial = d.get("en", "")

        if self.instance and self.instance.pk:
            prefill(self.instance.title, "title")
            prefill(self.instance.desc, "desc")
            prefill(self.instance.faq, "faq")

    def clean(self):
        cleaned = super().clean()

        def pack(prefix):
            return {
                "zh_Hant": cleaned.get(f"{prefix}_zh_Hant") or "",
                "zh_Hans": cleaned.get(f"{prefix}_zh_Hans") or "",
                "en": cleaned.get(f"{prefix}_en") or "",
            }

        cleaned["title"] = pack("title")
        cleaned["desc"] = pack("desc")
        cleaned["faq"] = pack("faq")

        return cleaned


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    form = TourAdminForm

    common_fields = (
        "tour_type",
        ("zh_Hant_translated", "zh_Hans_synced", "en_translated"),
        ("title_zh_Hant", "title_zh_Hans", "title_en"),
        ("desc_zh_Hant", "desc_zh_Hans", "desc_en"),
        ("faq_zh_Hant", "faq_zh_Hans", "faq_en"),
        ("price", "cover_image", "is_active"),
    )
    bus_only_fields = ("meeting_point", "pickup_time")
    cruise_only_fields = ("embark_port", "sail_date", "cabin_type")

    fieldsets = (
        ("基本設定 / 語言旗標", {"fields": common_fields}),
        ("巴士團專用", {"fields": bus_only_fields, "classes": ("bus-only",)}),
        ("郵輪團專用", {"fields": cruise_only_fields, "classes": ("cruise-only",)}),
    )

    list_display = ("__str__", "tour_type", "is_active", "updated_at")
    list_filter = ("tour_type", "is_active", "zh_Hans_synced", "en_translated")
    search_fields = ("title__zh_Hant", "title__en", "desc__zh_Hant", "desc__en")
    ordering = ("-updated_at", "-id")

    class Media:
        js = ("admin/tour_type_toggle.js",)
        css = {"all": ("admin/tour_type_toggle.css",)}
