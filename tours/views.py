from django.contrib.sites.models import Site
from django.conf import settings
from django.core.cache import cache
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeConfig, Channel
from .serializers import HomePayloadSerializer

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

CACHE_TTL = 60 * 5


@login_required
def member_dashboard(request):
    return render(request, "account/dashboard.html")


@login_required
def profile_view(request):
    if request.method == "POST":
        if "update_profile" in request.POST:
            form = UserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect("account_dashboard")
        elif "change_password" in request.POST:
            pwd_form = PasswordChangeForm(request.user, request.POST)
            if pwd_form.is_valid():
                user = pwd_form.save()
                update_session_auth_hash(request, user)  # 保持登入
                return redirect("account_dashboard")
    else:
        form = UserChangeForm(instance=request.user)
        pwd_form = PasswordChangeForm(request.user)

    return render(request, "account/profile.html", {
        "form": form,
        "pwd_form": pwd_form,
    })


def _site_from_request(request):
    host = request.get_host().split(":")[0]
    try:
        return Site.objects.get(domain=host)
    except Site.DoesNotExist:
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
# 我的訂單
@login_required
def orders_view(request):
    return render(request, "account/orders.html")

