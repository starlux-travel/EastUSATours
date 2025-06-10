from django.shortcuts import render
from .models import Tour, TourCategory

def home_view(request, lang='zh-hant'):
    categories = TourCategory.objects.all().order_by('id')
    category_sections = []

    for cat in categories:
        if lang == "en":
            tours = Tour.objects.filter(category=cat, is_active=True).only("title_en", "desc_en", "image", "price")[:6]
        else:
            tours = Tour.objects.filter(category=cat, is_active=True).only("title_zh_tw", "desc_zh_tw", "image", "price")[:6]
        category_sections.append({
            "category": cat,
            "tours": tours,
        })

    return render(request, "home.html", {
        "category_sections": category_sections,
        "lang": lang,
    })

# === 補上 search view（必須要有，否則會報錯） ===
def search(request):
    # 暫時不處理查詢，之後可加關鍵字條件
    return render(request, "search_results.html", {})
