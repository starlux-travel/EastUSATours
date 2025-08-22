# eastusatours/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 語系切換端點（/i18n/setlang/）
    path("i18n/", include("django.conf.urls.i18n")),
]

# 會自動加上 /zh-tw/, /zh-cn/, /en/ 前綴
urlpatterns += i18n_patterns(
    # 你的主站路由（首頁、會員中心…）
    path("", include("tours.urls")),

    # 帳號：登入/登出（模板路徑已用你現成檔名）
    path("accounts/login/",  auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),

    # 密碼重設流程（都放在 templates/auth/ 底下）
    path("accounts/reset/", auth_views.PasswordResetView.as_view(
        template_name="auth/password_reset_form.html"), name="password_reset"),
    path("accounts/reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="auth/password_reset_done.html"), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),
    path("accounts/reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="auth/password_reset_complete.html"), name="password_reset_complete"),

    # 後台
    path("admin/", admin.site.urls),
)

# 開發環境靜態/媒體
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
