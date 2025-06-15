from django.shortcuts import render
from .models import Tour, TourCategory

def home_view(request):
    lang = getattr(request, 'LANGUAGE_CODE', 'zh-hant')  # 取出目前語言
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
        "lang": lang,  # 一定要這行，template 才能判斷中英文
    })

def search(request):
    return render(request, "search_results.html", {})
