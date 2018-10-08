from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class Image(models.Model):
    '''
    This is image class model
    '''
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User)
    comment = models.TextField()
    likes = models.BooleanField(default=False)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image

    class Meta:
        ordering = ('-pub_date',)



    @classmethod
    def search_profile(cls, search_term):
        # cat = category.objects.get(name=search_term)
        profiles = cls.objects.filter(profile__icontains=search_term)
        return profiles

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__id=profile)
        return images

    @classmethod
    def update_caption(cls, update):
        pass


    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk=id)
        return comments

