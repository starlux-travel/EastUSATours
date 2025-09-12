from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "eastusatours.com",
    "www.eastusatours.com",
]

# PostgreSQL (Render 自動提供的 DATABASE_URL)
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# 靜態檔案
STATIC_ROOT = BASE_DIR / "staticfiles"

# CSRF / 安全設定
CSRF_TRUSTED_ORIGINS = [
    "https://eastusatours.com",
    "https://www.eastusatours.com",
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
