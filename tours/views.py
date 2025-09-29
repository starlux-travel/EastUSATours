from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Tour, DepartureCity, DepartureRegion

# 🔎 行程搜尋
def tour_search(request):
    q = request.GET.get("q")
    city_id = request.GET.get("city")
    region_id = request.GET.get("region")
    date = request.GET.get("date")
    promo = request.GET.get("promo")

    tours = Tour.objects.all()

    if q:
        # 假設 title/desc 是 JSONField，這裡用icontains查詢需視DB設定，簡化先用__icontains
        tours = tours.filter(title__icontains=q) | tours.filter(desc__icontains=q)

    if city_id:
        tours = tours.filter(city_id=city_id)

    if region_id:
        tours = tours.filter(city__region_id=region_id)

    if date:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            tours = tours.filter(departure_date__year=date_obj.year,
                                 departure_date__month=date_obj.month)
        except ValueError:
            pass

    if promo == "1":
        tours = tours.filter(is_promo=True)

    return render(request, "tours/tour_list.html", {
        "tours": tours,
        "search_mode": True,
        "keyword": q,
    })


# 📋 行程列表
def tour_list(request):
    tours = Tour.objects.filter(is_featured=True).order_by("-id")
    return render(request, "tours/tour_list.html", {"tours": tours, "search_mode": False})


# 📖 行程詳情
def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, "tours/tour_detail.html", {"tour": tour})
