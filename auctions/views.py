from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from .models import User,Auctions,Bid,Comments


def index(request):
    items=Auctions.objects.filter(status="open")
    return render(request, "auctions/index.html",{"items":items})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method=="POST" and request.user.is_authenticated:
        user=request.user
        title=request.POST["title"]
        description=request.POST["description"]
        image=request.POST["image"]
        category=request.POST["category"]
        time=datetime.now()
        bid = request.POST["bid"]
        bid=Bid(id=0,price=bid,bider=user)
        auction=Auctions(title=title,description=description,price=bid,image=image,time=time,category=category)
        bid.item=auction
        auction.save()
        bid.save()
        auction.owner.add(user)
    return render(request,"auctions/create.html")

def item(request, item_id):
    item=Auctions.objects.get(id=item_id)
    if request.method=="POST":
        action=request.POST["action"]
        if action=="addwatch":
            request.user.watchlist.add(item)
        elif action=="removewatch":
            request.user.watchlist.remove(item)
        elif action=="close":
            item.status="close"
            item.save()
        elif action=="bid":
            bid = request.POST["bid"]
            if float(bid)>item.price.price:
                bid=Bid(price=bid,bider=request.user,item=item)
                bid.save()
                item.price=bid
                item.save()
            else:
                return HttpResponse("Bids must be at least higher than current price")
        elif action=="comment":
            comment=request.POST["comment"]
            comment=Comments(text=comment,user=request.user,item=item)
            comment.save()
        elif action=="":
            return HttpResponse("{action}")
        return HttpResponseRedirect(reverse("item",args=[item_id]))
    return render(request,"auctions/item.html",
                  {"bid":Bid.objects.filter(item=item),
                    "item":item,
                   "watchlist":request.user.watchlist.all(),
                   "comments":item.comment.reverse()
                   })

def watchlist(request):
    return render(request,"auctions/watchlist.html",{"watchlist":request.user.watchlist.all()})
