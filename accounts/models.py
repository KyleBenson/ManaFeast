from django.contrib.gis.db import models
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Account(models.Model):

    """
    A donor or recipient, possibly an organization rather
    than a particular individual, that uses this service
    """

    phone_number = models.CharField(null=False, max_length=15)
    user = models.ForeignKey(User)


class Recipient(models.Model):

    """For example, a food bank"""

    lat = models.FloatField()
    lon = models.FloatField()

    distance_willing_to_travel = models.IntegerField(default=25) # in miles
    accepts_pickup = models.BooleanField(null=False, default=True)
    accepts_dropoff = models.BooleanField(null=False, default=True)


class Donor(models.Model):

    """For example, a restaurant or school."""

    lat = models.FloatField()
    lon = models.FloatField()

    distance_willing_to_travel = models.IntegerField(default=25) # in miles
    accepts_pickup = models.BooleanField(null=False, default=True)
    accepts_dropoff = models.BooleanField(null=False, default=True)


class AccountCreationForm(UserCreationForm):

    email = EmailField(required=True)
    phone_number = CharField(max_length=15)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['distance_willing_to_travel', 'accepts_pickup', 'accepts_dropoff']


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['distance_willing_to_travel', 'accepts_pickup', 'accepts_dropoff']
