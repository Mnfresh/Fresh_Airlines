from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_wallet')
    balance = models.FloatField(default=0.00)
    currency = models.CharField(default='EUR')
