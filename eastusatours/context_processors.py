from django.utils.translation import get_language
from tours.models import DepartureRegion
from cruise.models import CruiseRegion

# Django 語言代碼 → 網址語言代碼
REV_LANGUAGE_CODE_MAP = {
    "zh-hant": "tw",
    "zh-hans": "cn",
    "en": "en",
}

def regions_processor(request):
    return {
        "departure_regions": DepartureRegion.objects.prefetch_related("cities").all(),
        "cruise_regions": CruiseRegion.objects.prefetch_related("ports").all(),
    }

def current_lang(request):
    """
    提供 lang_prefix (tw/cn/en) 到所有 template
    """
    current_lang = get_language()  # zh-hant / zh-hans / en
    ext_lang = REV_LANGUAGE_CODE_MAP.get(current_lang, "en")
    return {
        "lang_prefix": ext_lang
    }
