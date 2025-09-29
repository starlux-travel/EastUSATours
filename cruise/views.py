from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import CruiseTour, CruiseRegion, CruisePort

# 郵輪列表
def cruise_list(request):
    cruises = CruiseTour.objects.all().order_by("-id")
    return render(request, "cruise/cruise_list.html", {"cruises": cruises})


# 郵輪搜尋
def cruise_search(request):
    q = request.GET.get("q")
    line = request.GET.get("line")
    region_id = request.GET.get("region")
    port_id = request.GET.get("port")
    month = request.GET.get("month")
    chinese = request.GET.get("chinese")
    special = request.GET.get("special")

    cruises = CruiseTour.objects.all()

    if q:
        cruises = cruises.filter(title__icontains=q) | cruises.filter(desc__icontains=q)

    if line:
        cruises = cruises.filter(line__icontains=line)

    if region_id:
        cruises = cruises.filter(port__region_id=region_id)

    if port_id:
        cruises = cruises.filter(port_id=port_id)

    if month:
        try:
            date_obj = datetime.strptime(month, "%Y-%m")
            cruises = cruises.filter(departure_date__year=date_obj.year,
                                     departure_date__month=date_obj.month)
        except ValueError:
            pass

    if chinese == "1":
        cruises = cruises.filter(has_chinese=True)

    if special == "1":
        cruises = cruises.filter(is_special=True)

    return render(request, "cruise/cruise_list.html", {"cruises": cruises, "search_mode": True})


# 郵輪詳細
def cruise_detail(request, pk):
    cruise = get_object_or_404(CruiseTour, pk=pk)
    return render(request, "cruise/cruise_detail.html", {"cruise": cruise})
