from django.urls import path

from .views import (
    HomeView,
    NoteCreateView,
    NoteDeleteView,
    NoteDetailView,
    NoteListView,
    NoteUpdateView,
    TripCreateView,
    TripDeleteView,
    TripDetailView,
    TripUpdateView,
    trip_list,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
    path("dashboard/note/", NoteListView.as_view(), name="note-list"),
    path("dashboard/note/create/", NoteCreateView.as_view(), name="note-create"),  # noqa E501
    path("dashboard/trip/create/", TripCreateView.as_view(), name="trip-create"),  # noqa E501
    path("dashboard/trip/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),  # noqa E501
    path("dashboard/trip/<int:pk>/update/", TripUpdateView.as_view(), name="trip-update"),  # noqa E501
    path("dashboard/trip/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"),  # noqa E501
    path("dashboard/note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),  # noqa E501
    path("dashboard/note/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),  # noqa E501
    path("dashboard/note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),  # noqa E501
]
