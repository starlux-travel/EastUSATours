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
    "django.contrib.sessions.middleware.SessionMiddleware",
    # 使用 Django 的 LocaleMiddleware（處理語言切換）
    "django.middleware.locale.LocaleMiddleware",
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
# 預設語言
LANGUAGE_CODE = "tw"

LANGUAGES = [
    ("tw", "繁體中文"),
    ("cn", "简体中文"),
    ("en", "English"),
]

# 語言檔位置
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
# 靜態檔案
# ================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ================
# 資料庫設定 (MySQL)
# ================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eastusatours',       # 資料庫名稱
        'USER': 'django_user',        # 你剛建立的使用者
        'PASSWORD': 'Django2025!',    # 使用者密碼
        'HOST': '127.0.0.1',          # 本機測試用
        'PORT': '3306',               # 預設 MySQL port
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
