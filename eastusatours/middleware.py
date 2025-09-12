# eastusatours/middleware.py
import re
from django.utils import translation

LANG_MAP = {"zh-tw": "zh-hant", "zh-cn": "zh-hans", "en": "en"}
LANG_PREFIX_RE = re.compile(r"^/(zh-tw|zh-cn|en)(/|$)")

class CustomLanguageMiddleware:
    """
    依 URL 前綴 /zh-tw|zh-cn|en 啟用對應語系
    並在 request 上提供：
      - request.LANGUAGE_CODE (DJ 語碼)
      - request.ext_lang      (URL 語碼：zh-tw/zh-cn/en)
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info or "/"
        m = LANG_PREFIX_RE.match(path)
        if m:
            ext = m.group(1)
            dj_lang = LANG_MAP.get(ext, "zh-hant")
            translation.activate(dj_lang)
            request.LANGUAGE_CODE = dj_lang
            request.ext_lang = ext
        else:
            request.ext_lang = None
        response = self.get_response(request)
        translation.deactivate()
        return response
