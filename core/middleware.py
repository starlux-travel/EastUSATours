from django.utils import translation

# 語言代碼映射
LANG_MAP = {
    "tw": "zh-hant",
    "cn": "zh-hans",
    "en": "en",
}

class LocaleFromPathMiddleware:
    """
    簡單的 Middleware：
    - 讀取網址第一段 (/tw, /cn, /en)
    - 設定 request.LANGUAGE_CODE
    - 沒有就預設 zh-hant
    """

    def __init__(self, get_response):
        self.get_response = get_response
        print("✅ LocaleFromPathMiddleware 載入成功")  # Debug 用

    def __call__(self, request):
        # 取 URL 第一段
        parts = request.path.strip("/").split("/", 1)
        lang = parts[0] if parts else None

        code = LANG_MAP.get(lang)
        if code:
            translation.activate(code)
            request.LANGUAGE_CODE = code
            request.lang_prefix = lang
        else:
            translation.activate("zh-hant")
            request.LANGUAGE_CODE = "zh-hant"
            request.lang_prefix = "tw"

        response = self.get_response(request)
        translation.deactivate()
        return response
