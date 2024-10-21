from django.urls import path

from .views import (
    HomeView,
    NoteCreateView,
    NoteDetailView,
    NoteListView,
    TripCreateView,
    TripDetailView,
    trip_list,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
    path("dashboard/note/", NoteListView.as_view(), name="note-list"),
    path("dashboard/note/create/", NoteCreateView.as_view(), name="note-create"),  # noqa E501
    path("dashboard/trip/create/", TripCreateView.as_view(), name="trip-create"),  # noqa E501
    path("dashboard/trip/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),  # noqa E501
    path("dashboard/note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),  # noqa E501
]
