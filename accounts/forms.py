from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "mobile"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded shadow-sm focus:ring focus:ring-blue-200"
            }),
            "mobile": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded shadow-sm focus:ring focus:ring-blue-200"
            }),
        }
