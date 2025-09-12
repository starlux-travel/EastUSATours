# tours/views.py
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .models import Tour, TourType
from .serializers import TourSerializer
from .utils import pick_lang

def home(request, *args, **kwargs):
    """首頁：依登入狀態顯示不同版本"""
    template = "tours/home_member.html" if request.user.is_authenticated else "tours/home_guest.html"
    return render(request, template, {})

def tour_list(request):
    """Tours 列表頁"""
    tours = Tour.objects.filter(is_active=True).order_by("-updated_at", "-id")[:20]
    return render(request, "tours/tour_list.html", {"tours": tours})

def tour_detail(request, pk):
    """Tours 詳細頁"""
    tour = Tour.objects.filter(pk=pk, is_active=True).first()
    return render(request, "tours/tour_detail.html", {"tour": tour})

class TourViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Tour.objects.filter(is_active=True).order_by("-updated_at", "-id")
    serializer_class = TourSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        req = self.request
        t = req.query_params.get("type")  # bus_tour / cruise_tour
        q = req.query_params.get("q")
        if t in (TourType.BUS, TourType.CRUISE):
            qs = qs.filter(tour_type=t)
        if q:
            lang = (req.query_params.get("lang") or "zh-Hant")
            key_map = {
                "zh-Hant": ("title__zh_Hant", "desc__zh_Hant"),
                "zh-Hans": ("title__zh_Hans", "desc__zh_Hans"),
                "en": ("title__en", "desc__en"),
            }
            k1, k2 = key_map.get(lang, ("title__zh_Hant", "desc__zh_Hant"))
            qs = qs.filter(Q(**{f"{k1}__icontains": q}) | Q(**{f"{k2}__icontains": q}))
        return qs

    @action(detail=True, methods=["get"])
    def display(self, request, pk=None):
        obj = self.get_object()
        lang = request.query_params.get("lang") or "zh-Hant"
        data = {
            "id": obj.id,
            "type": obj.tour_type,
            "title": pick_lang(obj.title or {}, lang),
            "desc": pick_lang(obj.desc or {}, lang),
            "faq": pick_lang(obj.faq or {}, lang),
        }
        return Response(data)
