from django.contrib.auth.models import AbstractUser
from django.db import models


class Auctions(models.Model):
    title=models.CharField(max_length=64)
    description=models.TextField()
    image=models.URLField()
    time=models.TimeField()
    category=models.ForeignKey("Categories",on_delete=models.SET_NULL,blank=True,null=True,related_name="item")
    status=models.CharField(max_length=64,default="open")
    def __str__(self):
        return self.title

class User(AbstractUser):
    own=models.ManyToManyField(Auctions,blank=True,null=True,related_name="owner")
    watchlist = models.ManyToManyField(Auctions,blank=True,null=True, related_name="watchlist")
    def __str__(self):
        return self.username

class Bid(models.Model):
    price=models.FloatField()
    bider=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Auctions,on_delete=models.CASCADE,related_name="price")
    def __str__(self):
        return str(self.price)

class Comments(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    item=models.ForeignKey(Auctions,on_delete=models.CASCADE,related_name="comment")
    def __str__(self):
        return f"{self.user.username}: {self.text}"

class Categories(models.Model):
    category=models.CharField(max_length=64)

    def __str__(self):
        return self.category