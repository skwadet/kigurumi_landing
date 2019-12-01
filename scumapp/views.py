from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def index(request):
    item = Item.objects.all()
    review = Review.objects.all()
    return render(request, 'index.htm', {'item': item, 'review': review})

