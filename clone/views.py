from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

import datetime as dt

# Create your views here.
def instagram(request):
    return render(request, 'instagram.html')


def all_images(request):
    images = Image.objects.all()

    return render(request, "all-images/today-images.html", {"images": images})

# def image_of_day(request):
#     date = dt.date.today()
#     images = Image.todays_image()
#     return render(request, 'instagram.html', {"date": date, "images": images})