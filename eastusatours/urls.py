# eastusatours/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

# /i18n/setlang/：語系切換 POST 會用到
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# 這裡的 path 都會自動加上 /zh-tw/、/zh-cn/、/en/ 前綴
urlpatterns += i18n_patterns(
    # 你的主站路由（含首頁），建議在 tours/urls.py 裡面定義 "" → HomeView
    path("", include("tours.urls")),

    # 帳號：登入/登出/重設密碼（放在語系前綴底下）
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),  # 會用 settings.LOGOUT_REDIRECT_URL
        name="logout",
    ),
    path(
        "accounts/reset/",
        auth_views.PasswordResetView.as_view(template_name="auth/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"),
        name="password_reset_complete",
    ),

    # 後台（也在語系前綴底下）
    path("admin/", admin.site.urls),
)

# 開發模式提供媒體檔案
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
