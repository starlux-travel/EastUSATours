from django import forms
from django.contrib.auth.models import User

from .models import Tour

# ✅ 這是你原本的
class YourProfileForm(forms.ModelForm):
    """用來修改會員基本資料的表單"""
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

# ✅ 新增：搜尋 Tour 用的表單
class TourSearchForm(forms.Form):
    region = forms.ChoiceField(
        choices=[('', '所有地區')] + Tour.REGION_CHOICES,
        required=False,
        label='地區'
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        label='目的城市'
    )
    keyword = forms.CharField(
        max_length=100,
        required=False,
        label='關鍵字'
    )
