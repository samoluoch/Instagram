from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    bio = models.TextField()


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
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comments = models.TextField()
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
