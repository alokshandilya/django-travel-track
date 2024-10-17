from django.urls import path

from .views import HomeView, trip_list

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
]
