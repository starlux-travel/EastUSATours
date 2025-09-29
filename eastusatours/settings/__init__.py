import os

# 讀取環境變數 DJANGO_ENV，決定載入哪個設定
# 預設是 local
DJANGO_ENV = os.getenv("DJANGO_ENV", "local")

if DJANGO_ENV == "production":
    from .production import *
else:
    from .local import *

