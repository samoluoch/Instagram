from django import forms
from .models import Image,Profile



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'pub_date', 'profile']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']