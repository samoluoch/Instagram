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



class Image(models.Model):
    '''
    This is image class model
    '''
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    caption = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.TextField()
    likes = models.BooleanField(default=False)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def todays_image(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date=today)
        return image

    @classmethod
    def search_by_profile(cls, search_term):
        # cat = category.objects.get(name=search_term)
        image = cls.objects.filter(profile__name__icontains=search_term)
        return image


    @classmethod
    def days_image(cls, date):
        image = cls.objects.filter(pub_date__date=date)
        return image

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images


class Comments(models.Model):
    comment = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk=id)
        return comments
