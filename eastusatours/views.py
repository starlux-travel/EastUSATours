from django.shortcuts import render
from tours.models import Tour

def home(request):
    # 郵輪
    tours_cruise = Tour.objects.filter(tour_type="cruise_tour")[:6]
    # 熱門行程（先簡單用 price 排序模擬）
    hot_tours = Tour.objects.order_by("-id")[:6]
    # 美國巴士
    tours_us = Tour.objects.filter(tour_type="bus_tour")[:6]
    # 歐洲（假設 category 欄位未來可用，先放空或用標籤）
    tours_eu = Tour.objects.none()

    context = {
        "tours_cruise": tours_cruise,
        "hot_tours": hot_tours,
        "tours_us": tours_us,
        "tours_eu": tours_eu,
    }
    return render(request, "tours/home_guest.html", context)
