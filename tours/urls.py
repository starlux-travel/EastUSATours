# tours/urls.py
from django.urls import path
from django.shortcuts import render
from .views import HomeView, member_dashboard

def site_home(request):
    # ✅ 回到用模板渲染
    return render(request, "home.html")

urlpatterns = [
    # 前台首頁（HTML）
    path("", site_home, name="home"),

    # API 首頁（JSON）
    path("api/home/", HomeView.as_view(), name="home_api"),

    # 會員中心（需登入）
    path("account/", member_dashboard, name="account"),
]
