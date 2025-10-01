import os
import dj_database_url
from .base import *

# ---------------------------
# 安全性設定
# ---------------------------
DEBUG = False

ALLOWED_HOSTS = [
    "eastusatours.onrender.com",
    os.getenv("RENDER_EXTERNAL_HOSTNAME", ""),
]

CSRF_TRUSTED_ORIGINS = [
    "https://eastusatours.onrender.com",
    f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME', '')}",
]

# ---------------------------
# 資料庫設定（Render 預設 PostgreSQL）
# ---------------------------
DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        ssl_require=True,
    )
}

# ---------------------------
# 靜態 / 媒體檔案
# ---------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static"   # 指到你現有的 static 資料夾
]
STATIC_ROOT = BASE_DIR / "staticfiles"          # collectstatic 輸出

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
# Email 設定（環境變數）
# ---------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "noreply@eastusatours.com")

# ---------------------------
# 靜態檔案壓縮（WhiteNoise）
# ---------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
