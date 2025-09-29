# core/redirect_lang.py
from django.shortcuts import redirect

class RedirectByBrowserLangMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ("/", ""):
            accept = (request.META.get("HTTP_ACCEPT_LANGUAGE") or "").lower()
            if any(k in accept for k in ["zh-hant", "zh-tw", "zh-hk"]):
                return redirect("/tw/")
            if any(k in accept for k in ["zh-hans", "zh-cn", "zh-sg"]):
                return redirect("/cn/")
            return redirect("/en/")
        return self.get_response(request)
