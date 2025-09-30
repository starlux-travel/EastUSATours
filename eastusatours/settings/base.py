from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# 專案根目錄
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-test-key-change-this-later"

# ================
# 已安裝應用程式
# ================
INSTALLED_APPS = [
    # Django 內建
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",   # ✅ Allauth 需要

    # 第三方套件
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # 專案應用
    "core",
    "tours.apps.ToursConfig",
    "cruise.apps.CruiseConfig",
]

# ================
# Middleware
# ================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # ✅ 靜態檔案處理
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",   # ✅ 語言切換
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "eastusatours.urls"

# ================
# Templates
# ================
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
                "eastusatours.context_processors.regions_processor",
            ],
        },
    },
]

# ================
# WSGI
# ================
WSGI_APPLICATION = "eastusatours.wsgi.application"

# ================
# 語言 / 國際化
# ================
LANGUAGE_CODE = "zh-hant"  # 預設繁中

LANGUAGES = [
    ("zh-hant", "繁體中文"),
    ("zh-hans", "简体中文"),
    ("en", "English"),

]
LOCALE_PATHS = [BASE_DIR / "locale"]

# ================
# 時區 / 時間
# ================
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ================
# Debug / Hosts
# ================
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# ================
# 靜態 / 媒體檔案
# ================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ Allauth 相關設定
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# ================
# （本地可選）MySQL 設定
# ================
# 如果要用 SQLite 就不用這段
# 本地開發用 MySQL 設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eastusatours',
        'USER': 'django_user',
        'PASSWORD': 'Django2025!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

