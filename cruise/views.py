from django.shortcuts import render, get_object_or_404
from .models import CruiseTour


# 🔍 搜尋郵輪
def cruise_search(request):
    keyword = request.GET.get("keyword", "")
    depart_date = request.GET.get("depart_date", "")
    city = request.GET.get("city", "")
    region = request.GET.get("region", "")

    cruises = CruiseTour.objects.filter(is_active=True)

    if keyword:
        cruises = cruises.filter(title__icontains=keyword)
    if city:
        cruises = cruises.filter(city__icontains=city)
    if region:
        cruises = cruises.filter(region__name__icontains=region)
    if depart_date:
        cruises = cruises.filter(depart_date=depart_date)

    return render(request, "cruise/cruise_list.html", {
        "cruises": cruises,
        "search_mode": True,
        "selected_city": city,
        "selected_date": depart_date,
        "keyword": keyword,
        "region": region,
    })


# 📋 郵輪列表
def cruise_list(request):
    cruises = CruiseTour.objects.filter(is_active=True).order_by("-id")
    return render(request, "cruise/cruise_list.html", {
        "cruises": cruises,
        "search_mode": False,
    })


# 📌 郵輪詳細
def cruise_detail(request, pk):
    cruise = get_object_or_404(CruiseTour, pk=pk)
    return render(request, "cruise/cruise_detail.html", {"cruise": cruise})
