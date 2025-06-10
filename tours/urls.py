from django.urls import path
from tours import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search, name='search'),
]
