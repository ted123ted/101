from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
# Create your views here.


class ShopView(ListView):
    model = Item
    template_name = "shop.html"





