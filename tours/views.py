# tours/views.py
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.cache import cache
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeConfig, Channel
from .serializers import HomePayloadSerializer
# tours/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def member_dashboard(request):
    return render(request, "account/dashboard.html")

CACHE_TTL = 60 * 5


def _site_from_request(request):
    host = request.get_host().split(":")[0]
    try:
        return Site.objects.get(domain=host)
    except Site.DoesNotExist:
        from django.conf import settings
        return Site.objects.get(id=getattr(settings, "SITE_ID", 1))

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
