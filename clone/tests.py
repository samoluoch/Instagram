from django.test import TestCase
from .models import Profile,Comments,Image

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new comment and saving it
        self.new_comment = Comments(name='nice image')
        self.new_location.save()


        # Creating a new image and saving it

        self.new_image= Image(name = 'Test Image',caption = 'This is a random test image')
        self.new_image.save()

        self.new_image.comment.add(self.comment)

    def tearDown(self):
        Image.objects.all().delete()
        Comments.objects.all().delete()
        Profile.objects.all().delete()

    def test_profile(self):
        images = Image.get_profile_images()
        self.assertTrue(len(images) > 0)



    def tearDown(self):
        Image.objects.all().delete()
        Comments.objects.all().delete()
        Profile.objects.all().delete()