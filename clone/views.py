from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

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


def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})


@login_required(login_url='/login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()

    return render(request, 'profile/upload_image.html', {'form': form})