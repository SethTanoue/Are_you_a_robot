import email
from unicodedata import name
from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    name = models.CharField(max_length=255)
    time = models.FloatField()
    email = models.EmailField(max_length=254)
