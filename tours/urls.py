# tours/urls.py
from django.urls import path
from django.shortcuts import render
from .views import HomeView, member_dashboard

# HTML 首頁（就地定義，不在 views.py 裡）
def site_home(request):
    return render(request, "home.html")

urlpatterns = [
    # 前台 HTML 首頁
    path("", site_home, name="home"),

    # API 首頁（JSON）
    path("api/home/", HomeView.as_view(), name="home_api"),

    # 會員中心（需登入）
    path("account/", member_dashboard, name="account"),
]
