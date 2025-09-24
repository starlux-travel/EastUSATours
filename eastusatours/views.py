from django.shortcuts import render
from tours.models import Tour, DepartureCity, Banner
from cruise.models import CruisePort

def home(request):
    # 出發城市 / 港口
    cities = DepartureCity.objects.select_related("region").all()
    ports = CruisePort.objects.select_related("region").all()

    # 熱門團
    qs = Tour.objects.filter(is_active=True)
    featured_tours = qs.order_by("-id")[:6]
    popular_tours = qs.order_by("-id")[:6]  # 之後可改 popularity 欄位

    # Banner
    banners = Banner.objects.filter(is_active=True).order_by("order")

    return render(request, "home.html", {
        "departure_cities": cities,
        "departure_ports": ports,
        "featured_tours": featured_tours,
        "popular_tours": popular_tours,
        "banners": banners,
    })
