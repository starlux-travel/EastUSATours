# tours/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.tour_search, name='tour_search'),
]
