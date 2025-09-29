from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [

    path("", lambda request: redirect("/tw/")),
    # 語言首頁，不再導到 zh-hant/ zh-hans
    path("tw/", core_views.home, {"lang_code": "tw"}, name="home_tw"),
    path("cn/", core_views.home, {"lang_code": "cn"}, name="home_cn"),
    path("en/", core_views.home, {"lang_code": "en"}, name="home_en"),

    # Django Admin
    path("admin/", admin.site.urls),

    # Tours 與 Cruise 模組
    path("tours/", include(("tours.urls", "tours"), namespace="tours")),
    path("cruise/", include(("cruise.urls", "cruise"), namespace="cruise")),
]



