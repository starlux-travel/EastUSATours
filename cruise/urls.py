from django.urls import path
from . import views

app_name = "cruise"

urlpatterns = [
    path("", views.cruise_list, name="list"),                 # /cruise/
    path("search/", views.cruise_search, name="cruise_search"),  # /cruise/search/
    path("<int:pk>/", views.cruise_detail, name="detail"),    # /cruise/1/
]
