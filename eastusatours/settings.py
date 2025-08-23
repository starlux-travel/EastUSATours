# eastusatours/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-please-change")

# 用環境變數控制 DEBUG（Render 上設 DEBUG=False / 本機可 True）
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1", "localhost",
    "eastusatours.com", "www.eastusatours.com",
    "eastusatours.onrender.com",
]

INSTALLED_APPS = [
    # Django 內建
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages",
    "django.contrib.staticfiles", "django.contrib.sites",
    # 你先裝著，之後要做 API 也方便，本機若沒裝就 pip install -r requirements.txt
    "rest_framework",
    # 你的 App
    "tours.apps.ToursConfig",
    "cart",
]
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # 靜態檔案
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/account/"
LOGOUT_REDIRECT_URL = "/"

ROOT_URLCONF = "eastusatours.urls"
WSGI_APPLICATION = "eastusatours.wsgi.application"

TEMPLATES = [{
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
}]

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "zh-tw"
LANGUAGES = [("zh-tw", "繁體中文（台灣）"), ("zh-cn", "简体中文（中国）"), ("en", "English")]
LOCALE_PATHS = [BASE_DIR / "locale"]
LANGUAGE_COOKIE_NAME = "django_language"
try:
    from django.conf.global_settings import PREFIX_DEFAULT_LANGUAGE  # noqa: F401
    PREFIX_DEFAULT_LANGUAGE = True  # type: ignore
except Exception:
    pass

# Static / Media
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "eastusatours-cache",
        "TIMEOUT": 300,
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": [], "DEFAULT_AUTHENTICATION_CLASSES": []}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
