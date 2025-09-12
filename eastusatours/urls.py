# eastusatours/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from tours.api import TourViewSet   # 👈 需要有 tours/api.py
from tours import views as tour_views   # 👈 指向首頁 home view

router = DefaultRouter()
router.register(r"tours", TourViewSet, basename="tour")

urlpatterns = [
    # 語言切換 API
    path("i18n/", include("django.conf.urls.i18n")),
    # API router
    path("api/", include(router.urls)),
]

# 多語路由
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", tour_views.home, name="home"),  # 👈 首頁對應 home view
    path("accounts/", include("accounts.urls")),
    path("tours/", include("tours.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
