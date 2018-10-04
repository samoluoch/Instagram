from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import ImageForm,EditProfileForm

import datetime as dt


@login_required(login_url='/login')
def instagram(request):
    images = Image.objects.all()
    return render(request,'instagram.html',{"images":images})


# def all_images(request):
#     images = Image.objects.all()
#
#     return render(request, "all-images/today-images.html", {"images": images})

# def image_of_day(request):
#     date = dt.date.today()
#     images = Image.todays_image()
#     return render(request, 'instagram.html', {"date": date, "images": images})


def profile(request, username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'
    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})

@login_required(login_url='/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = EditProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})

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












#returns all images
# def profile(request):
#     # profile = User.objects.get(username=username)
#     # try:
#     #     profile_details = Profile.get_by_id(profile.id)
#     # except:
#     #     profile_details = Profile.filter_by_id(profile.id)
#     images = Image.objects.all()
#     title = ' Instagram photos and videos'
#
#     return render(request, 'profile/profile.html', {'title':title,'images':images})