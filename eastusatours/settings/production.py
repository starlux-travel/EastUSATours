import os
from .base import *

# ---------------------------
# 安全性設定
# ---------------------------
DEBUG = False

ALLOWED_HOSTS = [
    "eastusatours.com",
    "www.eastusatours.com",
    os.getenv("RENDER_EXTERNAL_HOSTNAME", ""),  # ✅ Render 自動提供的 host
]

CSRF_TRUSTED_ORIGINS = [
    "https://eastusatours.com",
    "https://www.eastusatours.com",
    f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME', '')}",
]

# ---------------------------
# 資料庫設定（Render 預設 PostgreSQL）
# ---------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "eastusatours"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# ---------------------------
# 靜態 / 媒體檔案
# ---------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # 開發時 assets
STATIC_ROOT = BASE_DIR / "staticfiles"    # collectstatic 收集到這裡

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------
# 安全性 Header 與 Cookie
# ---------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# ---------------------------
# Email 設定（用環境變數）
# ---------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "noreply@eastusatours.com")
