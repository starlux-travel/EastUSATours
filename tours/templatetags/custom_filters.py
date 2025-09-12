# tours/templatetags/custom_filters.py
from django import template
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag(takes_context=True)
def lang_url(context, path: str):
    """
    產生帶語系前綴的網址。
    用法：
        {% load custom_filters %}
        <a href="{% lang_url '/account/login/' %}">登入</a>
    會輸出：
        /zh-tw/account/login/   或 /zh-cn/... /en/...
    """
    ext_lang = context.get("ext_lang", "zh-tw").strip("/")
    if not path.startswith("/"):
        path = "/" + path
    return f"/{ext_lang}{path}"

@register.filter
def active_if_eq(val, expected):
    """小工具：選單/語言切換時加上 'active'。"""
    return "active" if str(val) == str(expected) else ""

@register.simple_tag
def current_djlang():
    """
    回傳目前 Django 語系（zh-hant / zh-hans / en），
    有時你會想在模板判斷這個。
    """
    return get_language() or "zh-hant"
