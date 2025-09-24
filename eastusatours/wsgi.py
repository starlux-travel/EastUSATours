import os
from django.core.wsgi import get_wsgi_application

# 預設使用 production，若需要可手動改為 local
env = os.getenv("DJANGO_ENV", "production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eastusatours.settings")

application = get_wsgi_application()
