from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.cruise_search, name="cruise_search"),   # 🔍 搜尋
    path("list/", views.cruise_list, name="cruise_list"),         # 📋 列表
    path("<int:pk>/", views.cruise_detail, name="cruise_detail"), # 📌 詳細
]
