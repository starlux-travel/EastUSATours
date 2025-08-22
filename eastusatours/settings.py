# eastusatours/settings.py
from pathlib import Path
import os

# ── 基本 ───────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-please-change")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "eastusatours.com", "www.eastusatours.com",
                 "eastusatours.onrender.com"]

# ── App 清單 ───────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    # Django 內建
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # 第三方（若沒用可移除）
    "rest_framework",

    # 你的 App
    "tours.apps.ToursConfig",
    "cart",
]

SITE_ID = 1

# ── Middleware（LocaleMiddleware 要在 CommonMiddleware 之前）──────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",     # ← 必須在 CommonMiddleware 之前
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 登入/登出導向（會自動套在語系前綴底下）
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/account/"
LOGOUT_REDIRECT_URL = "/"

# ── URL / WSGI ────────────────────────────────────────────────────────────────
ROOT_URLCONF = "eastusatours.urls"
WSGI_APPLICATION = "eastusatours.wsgi.application"

# ── Templates ─────────────────────────────────────────────────────────────────
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

# ── DB（本機用 SQLite；上線改你的 DB）───────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ── 密碼規則 ───────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ── i18n / l10n（網址使用 zh-tw / zh-cn / en）──────────────────────────────────
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

# 預設語言：繁中台灣；網址也要有前綴（/zh-tw/）
LANGUAGE_CODE = "zh-tw"
LANGUAGES = [
    ("zh-tw", "繁體中文（台灣）"),
    ("zh-cn", "简体中文（中国）"),
    ("en", "English"),
]
LOCALE_PATHS = [BASE_DIR / "locale"]

# 讓「預設語言」也帶前綴（/zh-tw/）
# Django 4.2+ 可用；如無此設定也沒關係，預設為 True
try:
    from django.conf.global_settings import PREFIX_DEFAULT_LANGUAGE  # noqa
    PREFIX_DEFAULT_LANGUAGE = True  # type: ignore
except Exception:
    pass

LANGUAGE_COOKIE_NAME = "django_language"

# ── Static / Media ────────────────────────────────────────────────────────────
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── 快取（本機）───────────────────────────────────────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "eastusatours-cache",
        "TIMEOUT": 300,
    }
}

# ── 開發用信件（印在 console）───────────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ── DRF（若有用）──────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
