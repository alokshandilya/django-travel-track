from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Note, Trip


class HomeView(TemplateView):
    template_name = "trip/index.html"


def trip_list(request):
    if not request.user.is_authenticated:
        return render(request, "trip/index.html")
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips,
    }
    return render(request, "trip/trip_list.html", context)


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    fields = ["city", "country", "start_date", "end_date"]  # not owner
    # template -> model_form.html -> trip_form.html

    def form_valid(self, form):  # override form_valid method
        form.instance.owner = self.request.user  # set owner to current user
        # call parent form_valid method to save the form
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip

    # to display notes in the trip detail view
    def get_context_data(self, **kwargs):  # override get_context_data method
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        notes = trip.notes.all()  # because of related_name="notes" in Note
        context["notes"] = notes

        return context


class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    fields = ["city", "country", "start_date", "end_date"]
    # template -> model_form.html -> trip_form.html


class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    # template -> trip_confirm_delete.html


class NoteDetailView(DetailView):
    model = Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):  # override get_queryset method
        # only show notes that belong to the current user
        # trip__owner (double underscore) is a lookup that follows
        # relationships, (can use any field from the related model)
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"

    # show trips that belong to the current logged in user
    def get_form(self):  # override get_form method
        form = super(NoteCreateView, self).get_form()  # get form from parent
        trips = Trip.objects.filter(owner=self.request.user)

        # set queryset of trip field to show trips belonging to current user
        # it will be a dropdown list of trips
        form.fields["trip"].queryset = trips

        return form


# mostly the same as NoteCreateView
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"
    # uses same template as NoteCreateView, note_form.html
    # add button to the form to update the note

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips

        return form


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")
    # template -> note_confirm_delete.html
