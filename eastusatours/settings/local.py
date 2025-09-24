from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# 開發用 SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ✅ 靜態檔修正：改用根目錄 static/
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR.parent / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ 媒體檔
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 開發用 Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
