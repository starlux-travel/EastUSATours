# eastusatours/settings.py
from pathlib import Path
import os

# ── 基本 ───────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-please-change")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "eastusatours.com", "www.eastusatours.com"]

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

    # 第三方
    "rest_framework",

    # 你的 App
    "tours.apps.ToursConfig",
    "cart",
]

SITE_ID = 1

# ── Middleware（唯一一份，順序正確）──────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",   # 在 CommonMiddleware 之前
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 登入後/登出後導向
LOGIN_REDIRECT_URL = "/account/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "login"   # LoginRequiredMixin 會用到

# ── URL / WSGI ────────────────────────────────────────────────────────────────
ROOT_URLCONF = "eastusatours.urls"
WSGI_APPLICATION = "eastusatours.wsgi.application"

# ── Email（開發：輸出到 console）──────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# 正式寄信（備忘）
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "your@gmail.com"
# EMAIL_HOST_PASSWORD = "app-password"
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

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

# ── DB（本機 SQLite）──────────────────────────────────────────────────────────
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

# ── i18n / l10n（zh-tw / zh-cn / en）──────────────────────────────────────────
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

LANGUAGE_CODE = "zh-tw"
LANGUAGES = [
    ("zh-tw", "繁體中文（台灣）"),
    ("zh-cn", "简体中文（中国）"),
    ("en", "English"),
]
LOCALE_PATHS = [BASE_DIR / "locale"]

# ── Static / Media ────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── 快取（本機記憶體）──────────────────────────────────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "eastusatours-cache",
        "TIMEOUT": 300,
    }
}

# ── 可配置購物車商品模型 ─────────────────────────────────────────────────────
CART_PRODUCT_MODEL = "tours.SectionCard"

# ── DRF ───────────────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

# ── 其他 ───────────────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
