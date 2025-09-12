# accounts/urls.py
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("orders/", views.orders, name="orders"),

    # django-allauth 內建登入/登出/註冊
    path("", include("allauth.urls")),
]
