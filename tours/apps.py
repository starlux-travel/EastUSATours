# tours/apps.py
from django.apps import AppConfig

class ToursConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tours"

    def ready(self):
        # 啟用 signals（此檔為 no-op，不會拋錯）
        try:
            from . import signals  # noqa: F401
        except Exception:
            # 保底容錯：就算意外失敗，也不要讓專案起不來
            pass
