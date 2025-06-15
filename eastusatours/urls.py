from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

# 多語言切換路由
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # 主網址自動導向 /zh-hant/
    path('', RedirectView.as_view(url='/zh-hant/', permanent=True)), 
]

# 主多語路徑
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
)

# 靜態/媒體檔案開發時自動加載
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
