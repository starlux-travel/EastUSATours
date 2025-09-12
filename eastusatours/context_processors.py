# eastusatours/context_processors.py
def current_lang(request):
    """
    在模板提供 ext_lang（zh-tw/zh-cn/en）
    """
    return {"ext_lang": getattr(request, "ext_lang", None)}
