from django.urls import path
from . import views

urlpatterns = [
    path("", views.tour_list, name="tours_index"), 
    path("search/", views.tours_search, name="tours_search"),   # 🔍 搜尋
    path("list/", views.tour_list, name="tour_list"),           # 📋 列表
    path("<int:pk>/", views.tour_detail, name="tour_detail"),   # 📌 詳細頁
]
