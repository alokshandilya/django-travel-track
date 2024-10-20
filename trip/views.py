from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        notes = trip.notes.all()  # because of related_name="notes" in Note
        context["notes"] = notes

        return context


class NoteDetailView(DetailView):
    model = Note
