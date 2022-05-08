from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Auctions(models.Model):
    title=models.CharField(max_length=64)
    price=models.FloatField()
    description=models.TextField()
    image=models.URLField()
    time=models.TimeField()
    category=models.URLField()

