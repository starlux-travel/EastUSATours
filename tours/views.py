# tours/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.conf import settings

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeConfig, Channel
from .serializers import HomePayloadSerializer

CACHE_TTL = 60 * 5

def _site_from_request(request):
    host = request.get_host().split(":")[0]
    try:
        return Site.objects.get(domain=host)
    except Site.DoesNotExist:
        return Site.objects.get(id=getattr(settings, "SITE_ID", 1))

# ✅ 首頁：改成「把資料丟進 template」的 SSR 版本
def site_home(request):
    site = _site_from_request(request)
    channel = request.GET.get("channel", Channel.B2C)

    cfg = (
        HomeConfig.objects
        .filter(site=site, channel=channel)
        .prefetch_related("sections__cards")
        .first()
    )
    payload = HomePayloadSerializer(cfg).data if cfg else {
        "hero_title": "",
        "hero_subtitle": "",
        "hero_bg_image": "",
        "show_breadcrumbs": False,
        "seo_title": "",
        "seo_description": "",
        "seo_keywords": "",
        "sections": []
    }
    return render(request, "home.html", {"home": payload})

# 保留：首頁 JSON API（若前端需要）
class HomeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        channel = request.query_params.get("channel", Channel.B2C)
        site = _site_from_request(request)

        key = f"home:{site.id}:{channel}"
        data = cache.get(key)
        if not data:
            cfg = (
                HomeConfig.objects
                .filter(site=site, channel=channel)
                .prefetch_related("sections__cards")
                .first()
            )
            if not cfg:
                return Response({"sections": []})
            data = HomePayloadSerializer(cfg).data
            cache.set(key, data, CACHE_TTL)
        return Response(data)

@login_required
def member_dashboard(request):
    return render(request, "account/dashboard.html")
