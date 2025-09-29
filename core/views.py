from django.shortcuts import render, redirect
from django.utils.translation import get_language, activate
from .models import Banner, FAQ
from tours.models import Tour, DepartureRegion
from cruise.models import CruiseTour, CruiseRegion, CruisePort

# 🌐 語言代碼映射
LANGUAGE_CODE_MAP = {
    "tw": "zh-hant",
    "cn": "zh-hans",
    "en": "en",
}

def home(request, lang_code=None):
    """
    首頁：
    - 顯示 banners, tours, cruises, faqs
    - 語言由 middleware 控制
    """
    lang = get_language()

    # 🔧 修正 banners / faqs 排序欄位
    banners = Banner.objects.filter(is_active=True).order_by("order")[:6]
    faqs = FAQ.objects.all().order_by("order")[:6]

    featured_tours = Tour.objects.all().order_by("-id")[:6]
    popular_tours = Tour.objects.all().order_by("views")[:6] if hasattr(Tour, "views") else []
    featured_cruises = CruiseTour.objects.all().order_by("-id")[:6]

    # 搜尋器選項
    departure_regions = DepartureRegion.objects.prefetch_related("cities").all()
    tour_regions = DepartureRegion.objects.all()
    cruise_regions = CruiseRegion.objects.all()
    cruise_ports = CruisePort.objects.select_related("region").all()
    cruise_lines = CruiseTour.objects.values_list("line", flat=True).distinct()

    return render(request, "home.html", {
        "lang": lang,
        "lang_prefix": getattr(request, "lang_prefix", "en"),
        "banners": banners,
        "faqs": faqs,
        "featured_tours": featured_tours,
        "popular_tours": popular_tours,
        "featured_cruises": featured_cruises,
        "departure_regions": departure_regions,
        "tour_regions": tour_regions,
        "cruise_regions": cruise_regions,
        "cruise_ports": cruise_ports,
        "cruise_lines": cruise_lines,
    })


def switch_language(request, lang_code):
    """
    切換語言：支援 tw/cn/en → 轉換成 Django 認得的代碼
    """
    real_lang = LANGUAGE_CODE_MAP.get(lang_code, "en")  # 預設英文
    activate(real_lang)
    request.session["django_language"] = real_lang

    # 回到來源頁（或首頁）
    return redirect(request.META.get("HTTP_REFERER", f"/{lang_code}/"))
