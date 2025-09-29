from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    path("", views.tour_list, name="list"),                  # /tours/
    path("search/", views.tour_search, name="tour_search"),  # /tours/search/
    path("<int:pk>/", views.tour_detail, name="tour_detail"),  # /tours/1/
]
