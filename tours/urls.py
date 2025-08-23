from django.urls import path
from .views import site_home, member_dashboard, profile_view, orders_view

urlpatterns = [
    path("", site_home, name="home"),
    path("account/", member_dashboard, name="account_dashboard"),
    path("account/profile/", profile_view, name="account_profile"),
    path("account/orders/", orders_view, name="account_orders"),
]
