from django.shortcuts import render, get_object_or_404
from datetime import datetime

# ✅ 匯入模型
from core.models import Banner, FAQ
from tours.models import Tour
from cruise.models import CruiseTour


# ======================
# 首頁
# ======================
def home(request, lang_code=None):
    banners = Banner.objects.filter(is_active=True).order_by("order")
    faqs = FAQ.objects.all().order_by("order")
    tours = Tour.objects.all()[:6]
    cruises = CruiseTour.objects.all()[:6]
    popular_tours = Tour.objects.order_by("-views_count")[:5]

    context = {
        "banners": banners,
        "faqs": faqs,
        "featured_tours": tours,
        "featured_cruises": cruises,
        "popular_tours": popular_tours,
        "lang_code": lang_code,  # 可以傳給模板用
    }
    return render(request, "home.html", context)


# ======================
# 郵輪列表
# ======================
def cruise_list(request):
    cruises = CruiseTour.objects.all()
    return render(request, "cruise/cruise_list.html", {"cruises": cruises})


# ======================
# 郵輪搜尋
# ======================
def cruise_search(request):
    query = request.GET.get("q")
    city = request.GET.get("city")
    depart_date = request.GET.get("depart_date")

    cruises = CruiseTour.objects.all()

    if query:
        cruises = cruises.filter(title__icontains=query)

    if city:
        cruises = cruises.filter(description__icontains=city)

    if depart_date:
        try:
            date_obj = datetime.strptime(depart_date, "%Y-%m-%d")
            cruises = cruises.filter(
                departure_date__year=date_obj.year,
                departure_date__month=date_obj.month
            )
        except ValueError:
            pass

    return render(request, "cruise/cruise_search.html", {"cruises": cruises})


# ======================
# 郵輪詳細
# ======================
def cruise_detail(request, pk):
    cruise = get_object_or_404(CruiseTour, pk=pk)
    return render(request, "cruise/cruise_detail.html", {"cruise": cruise})
