# eastusatours/admin.py
from django.contrib import admin
from .models import Tour
from django import forms

class TourAdminForm(forms.ModelForm):
    copy_to_zh_cn = forms.BooleanField(required=False, label="複製繁中 → 簡中")
    copy_to_en = forms.BooleanField(required=False, label="複製繁中 → 英文")

    class Meta:
        model = Tour
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("copy_to_zh_cn"):
            cleaned_data["title_zh_cn"] = cleaned_data.get("title_zh_tw", "")
            cleaned_data["description_zh_cn"] = cleaned_data.get("description_zh_tw", "")
        if cleaned_data.get("copy_to_en"):
            cleaned_data["title_en"] = cleaned_data.get("title_zh_tw", "")
            cleaned_data["description_en"] = cleaned_data.get("description_zh_tw", "")
        return cleaned_data

class TourAdmin(admin.ModelAdmin):
    form = TourAdminForm
    list_display = ('title_zh_tw', 'is_featured')

admin.site.register(Tour, TourAdmin)
