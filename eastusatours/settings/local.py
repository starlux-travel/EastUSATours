from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# SQLite 本地使用
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 靜態檔案
STATICFILES_DIRS = [BASE_DIR / "static"]

# Email (本地測試用 Console)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
