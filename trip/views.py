from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip


class HomeView(TemplateView):
    template_name = "trip/index.html"


def trip_list(request):
    trips = Trip.objects.all()
    context = {
        "trips": trips,
    }
    return render(request, "trip/trip_list.html", context)
