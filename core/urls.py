from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView
from core import views as core_views

urlpatterns = [
    # 語言切換
    path("switch-language/<str:lang_code>/", core_views.switch_language, name="switch_language"),

        # 🔥 新增 Redirect
    path("tw/", RedirectView.as_view(url="/zh-hant/", permanent=True)),
    path("cn/", RedirectView.as_view(url="/zh-hans/", permanent=True)),
]

# 🌐 國際化 URL
urlpatterns += i18n_patterns(
    path("", core_views.home, name="home"),
    path("tours/", include(("tours.urls", "tours"), namespace="tours")),
    path("cruise/", include(("cruise.urls", "cruise"), namespace="cruise")),
    prefix_default_language=False,  # 預設語言不加前綴
)
