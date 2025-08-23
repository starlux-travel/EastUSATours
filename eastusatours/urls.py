from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

# 🔹 非語系前綴路由：語言切換用
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# 🔹 語系開頭的路由（會變成 /zh-tw/ /en/）
urlpatterns += i18n_patterns(
    path("", include("tours.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/reset/", auth_views.PasswordResetView.as_view(template_name="auth/password_reset_form.html"), name="password_reset"),
    path("accounts/reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),
    path("accounts/reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name="password_reset_complete"),
    path("admin/", admin.site.urls),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
