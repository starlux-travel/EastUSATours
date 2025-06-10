from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

# 多語言管理後台標題
admin.site.site_header = _("EastUSA Tours 管理後台")
admin.site.site_title = _("EastUSA Tours 系統")
admin.site.index_title = _("歡迎使用旅遊網站後台")

# 語言切換機制
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # 語言切換 POST 路由
]

# 多語言支援路由（會有 /en/、/zh-hant/ 前綴）
from django.conf.urls.i18n import i18n_patterns

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),  # 主 app 路由
    path('cart/', include('cart.urls', namespace='cart')),

)

# 開發環境靜態媒體處理
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
