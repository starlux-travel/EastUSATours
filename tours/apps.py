# tours/apps.py
from django.apps import AppConfig

class ToursConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tours"

    def ready(self):
        # 啟用快取失效 signals
        from . import signals  # noqa
