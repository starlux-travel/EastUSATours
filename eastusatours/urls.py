from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core import views as core_views

urlpatterns = [
    # 預設導向 → /tw/
    path("", lambda request: redirect("/tw/")),

    # 多語言首頁
    path("tw/", core_views.home, {"lang_code": "tw"}, name="home_tw"),
    path("cn/", core_views.home, {"lang_code": "cn"}, name="home_cn"),
    path("en/", core_views.home, {"lang_code": "en"}, name="home_en"),

    # 後台管理
    path("admin/", admin.site.urls),

    # Accounts (登入 / 註冊)
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),

    # Tours 模組
    path("tours/", include(("tours.urls", "tours"), namespace="tours")),

    # Cruise 模組
    path("cruise/", include(("cruise.urls", "cruise"), namespace="cruise")),
]
