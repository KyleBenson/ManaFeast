from django.contrib.gis.db import models
from datetime import datetime, timedelta
import accounts.models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Donation(models.Model):

    """
    Represents a food donation available for pick-up
    """

    lat = models.FloatField()
    lon = models.FloatField()

    long_description = models.TextField()
    short_description = models.TextField(max_length=50, null=False)

    time_window_start = models.DateTimeField(null=False, default=datetime.now())
    time_window_end = models.DateTimeField(null=True, default=datetime.now() + timedelta(hours=24))

    food_type = models.CharField(max_length=20, null=False)

    pickup = models.BooleanField(default=True)
    dropoff = models.BooleanField(default=True)

    user = models.ForeignKey(User, null=False)

    # required for GIS queries
    objects = models.GeoManager()

    def __str__(self):
        return 'Donation "%s" at (%f, %f): %s' % (self.short_description, self.lat, self.lon, self.long_description)

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['lat', 'lon', 'long_description', 'short_description',
                  'time_window_start', 'time_window_end', 'pickup', 'dropoff']

