from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import ImageForm,EditProfileForm,RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from .emails import activation_email

import datetime as dt


@login_required(login_url='/login')
def instagram(request):
    images = Image.objects.all()
    return render(request,'instagram.html',{"images":images})




def profile(request):
    profile = User.objects.get(username=request.user)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'
    print(images)
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
            return redirect('profile')
    else:
        form = ImageForm()

    return render(request, 'profile/upload_image.html', {'form': form})



def register(request):
    if request.user.is_authenticated():
        return redirect('instagram')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                activation_email(user, current_site, to_email)
                return HttpResponse('Confirm your email address to complete registration')
        else:
            form = RegistrationForm()
            return render(request, 'registration/signup.html',{'form':form})

def search_profile(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})

