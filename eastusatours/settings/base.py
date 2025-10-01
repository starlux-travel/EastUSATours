import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 安全性設定
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# 📦 已安裝的應用
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # allauth 需要的
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # 你自己的 app
    "core",
    "accounts",
    "tours",
    "cruise",
]

# 🛡️ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "eastusatours.urls"

# 🎨 Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "eastusatours.wsgi.application"

# 🗄️ Database
if os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            env="DATABASE_URL", conn_max_age=600, ssl_require=True
        )
    }
    print("🚀 使用 Render 的 PostgreSQL (DATABASE_URL)")
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "eastusatours",
            "USER": "django_user",
            "PASSWORD": "Django2025!",
            "HOST": "127.0.0.1",
            "PORT": "3306",
            "OPTIONS": {
                "charset": "utf8mb4",
            },
        }
    }
    print("💻 使用本地 MySQL")

# 🌏 語言 & 時區
LANGUAGE_CODE = "zh-hant"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 📂 靜態檔 & 媒體檔
STATIC_URL = "/static/"

# ⚡ 修正這裡，指到真正有 css/images 的 static 資料夾
STATICFILES_DIRS = [
    BASE_DIR / "eastusatours" / "static",
]

# collectstatic 會輸出到這裡（給 Render 用）
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 🆔 自動主鍵
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# allauth 需要的設定
SITE_ID = 1
