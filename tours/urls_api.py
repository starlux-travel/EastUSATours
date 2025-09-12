# tours/urls.py
from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    # 首頁（由 eastusatours/urls.py 指向這裡）
    path("", views.home, name="home"),

    # Tours 列表
    path("list/", views.tour_list, name="tour_list"),

    # Tours 詳細頁（依照 ID）
    path("<int:pk>/", views.tour_detail, name="tour_detail"),
]
