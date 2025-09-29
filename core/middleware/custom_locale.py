# core/custom_locale.py
from django.utils import translation

LANG_MAP = {"tw": "zh-hant", "cn": "zh-hans", "en": "en"}
REV_LANG_MAP = {v: k for k, v in LANG_MAP.items()}


class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path_parts = request.path.strip("/").split("/")
        real_lang = None

        # 1) 優先讀網址前綴
        if path_parts and path_parts[0] in LANG_MAP:
            prefix = path_parts[0]
            real_lang = LANG_MAP[prefix]
            request.lang_prefix = prefix
        else:
            # 2) 其次讀 session 既有語言
            sess_lang = request.session.get("django_language")
            if sess_lang:
                real_lang = sess_lang
                request.lang_prefix = REV_LANG_MAP.get(sess_lang, "en")
            else:
                request.lang_prefix = "en"

        if real_lang:
            translation.activate(real_lang)
            request.LANGUAGE_CODE = real_lang

        response = self.get_response(request)
        translation.deactivate()
        return response
