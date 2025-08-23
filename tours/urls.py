from django.urls import path
from django.shortcuts import render
from .views import HomeView, member_dashboard, profile_view

def site_home(request):
    return render(request, "home.html")

urlpatterns = [
    # 首頁（HTML）
    path("", site_home, name="home"),

    # API 首頁（JSON）
    path("api/home/", HomeView.as_view(), name="home_api"),

    # 會員中心（需登入）
    path("account/", member_dashboard, name="account_dashboard"),

    # 個人資料（需登入）
    path("account/profile/", profile_view, name="account_profile"),

    path("account/orders/", orders_view, name="account_orders"),

    
]
