from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Tour

def tours_search(request):
    keyword = request.GET.get("keyword", "")
    depart_date = request.GET.get("depart_date", "")
    city = request.GET.get("city", "")
    region = request.GET.get("region", "")

    tours = Tour.objects.filter(is_active=True)

    if keyword:
        tours = tours.filter(
            Q(title_zh_hant__icontains=keyword) |
            Q(title_zh_hans__icontains=keyword) |
            Q(title_en__icontains=keyword)
        )
    if city:
        tours = tours.filter(departure_city__id=city)
    if region:
        tours = tours.filter(departure_region__id=region)
    if depart_date:
        tours = tours.filter(departure_date=depart_date)

    return render(request, "tours/tour_list.html", {
        "tours": tours,
        "search_mode": True,
        "selected_city": city,
        "selected_date": depart_date,
        "keyword": keyword,
        "region": region,
    })

def tour_list(request):
    tours = Tour.objects.filter(is_active=True).order_by("-id")
    return render(request, "tours/tour_list.html", {"tours": tours, "search_mode": False})

def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk, is_active=True)
    return render(request, "tours/tour_detail.html", {"tour": tour})
