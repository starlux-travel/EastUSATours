from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-test-key-change-this-later"

INSTALLED_APPS = [
    # Django 內建
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",   # ✅ 必須保留，Allauth 需要

    # 第三方套件
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # 你的應用
    "tours.apps.ToursConfig",
    "cruise.apps.CruiseConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # ← 加這行
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # allauth 需要的 middleware
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "eastusatours.urls"

TEMPLATES  = [
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

# ---------------------------
# 語言 / 國際化
# ---------------------------
LANGUAGES = [
    ("zh-hant", "Traditional Chinese"),
    ("zh-hans", "Simplified Chinese"),
    ("en", "English"),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---------------------------
# 靜態檔案設定
# ---------------------------
STATICFILES_DIRS = [BASE_DIR / "static"]   # 專案內的 static/
STATIC_ROOT = BASE_DIR / "staticfiles"

# ---------------------------
# 媒體檔案設定
# ---------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ 必須保留，否則 allauth 會失敗
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
