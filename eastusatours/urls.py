from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),  # 導向 tours app（首頁、行程列表等）
]

# 靜態媒體（可選）
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 多語言 admin 翻譯
admin.site.site_header = _("EastUSA Tours 管理後台")
admin.site.site_title = _("EastUSA Tours 系統")
admin.site.index_title = _("歡迎使用旅遊網站後台")


