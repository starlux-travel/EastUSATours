# eastusatours/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from tours.api import TourViewSet
from eastusatours import views as core_views   # 👈 改成主專案 views

# 建立 API router
router = DefaultRouter()
router.register(r"tours", TourViewSet, basename="tour")

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", include(router.urls)),
]

# 多語言路由
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", core_views.home, name="home"),   # 👈 改成 eastusatours/views.py
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("tours/", include("tours.urls")),
    path("cruise/", include("cruise.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
