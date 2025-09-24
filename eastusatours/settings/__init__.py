import os

# 預設 local，伺服器可以設定 DJANGO_ENV=production
env = os.getenv("DJANGO_ENV", "local")

if env == "production":
    from .production import *
else:
    from .local import *
