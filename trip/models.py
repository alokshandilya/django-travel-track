from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trips",  # access trips from user instance (user.trips)
    )

    def __str__(self):
        return self.city


class Note(models.Model):
    EXCURSIONS = (
        ("event", "Event"),
        ("dining", "Dining"),
        ("experience", "Experience"),
        ("general", "General"),
    )

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="notes",  # access notes from trip instance (trip.notes)
    )
    description = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSIONS)
    img = models.ImageField(upload_to="notes", blank=True, null=True)
    rating = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.name} in {self.trip.city}"
