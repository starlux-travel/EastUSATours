# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('add/<int:tour_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:tour_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
]
