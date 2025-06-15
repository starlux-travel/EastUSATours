from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),    # 首頁
    path('search/', views.search, name='search'),  # 搜尋
    # 之後再加更多細節路由
]