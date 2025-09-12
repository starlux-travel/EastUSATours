# tours/urls.py
from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    path("", views.home, name="home"),              # 首頁
    path("list/", views.tour_list, name="tour_list"),  # Tours 列表
    path("<int:pk>/", views.tour_detail, name="tour_detail"),  # Tours 詳細頁
]
