from django.contrib.auth.models import User
from django.db import models

CURRENCY_CHOICES = [
    ('USD', 'USD - United States Dollar'),
    ('GBP', 'GBP - British Pound'),
    ('EUR', 'EUR - Euro'),
    ('BGN', 'BGN - Bulgarian Lev'),
]

class Ticket(models.Model):

    start_country = models.CharField(max_length=60)
    start_city = models.CharField(max_length=60)
    start_airport = models.CharField(max_length=100)
    end_country = models.CharField(max_length=60)
    end_city = models.CharField(max_length=60)
    end_airport = models.CharField(max_length=100)
    date_and_time_of_take_off = models.DateTimeField()
    date_and_time_of_arrival = models.DateTimeField()
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0.00)
    currency = models.CharField(choices=CURRENCY_CHOICES)
    place_in_plane = models.IntegerField(default=0)
    additional_baggage = models.BooleanField(default=False)
    details = models.TextField(blank=True, null=True)


class PurchasedTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
