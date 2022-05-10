from django.contrib.auth.models import AbstractUser
from django.db import models


class Auctions(models.Model):
    title=models.CharField(max_length=64)
    price=models.FloatField()
    description=models.TextField()
    image=models.URLField()
    time=models.TimeField()
    category=models.URLField()

class User(AbstractUser):
    own=models.ManyToManyField(Auctions,blank=True,related_name="owner")
    watchlist = models.ManyToManyField(Auctions, blank=True, related_name="watchlist")

