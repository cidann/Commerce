from django.contrib import admin
from django import forms
from .models import *
# Register your models here.


admin.site.register(Auctions)
admin.site.register(Comments)
admin.site.register(Bid)