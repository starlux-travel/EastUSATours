from django import forms
from django.contrib.auth.models import User

class YourProfileForm(forms.ModelForm):
    """用來修改會員基本資料的表單"""
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
