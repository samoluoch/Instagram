from django.test import TestCase
from .models import Profile,Comments,Image

# Create your tests here.
class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.samsoluoch = Profile(bio = 'samsoluoch')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.samsoluoch,Profile))
    #testing save method
    def test_save_profile(self):
        self.samsoluoch.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    #testng for deleting method
    def test_delete_profile(self):
        self.samsoluoch.save_profile()
        self.samsoluoch.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)

class CommentTestClass(TestCase):
    #set up method
    def setUp(self):
        self.testcomment = Comments(comments = 'testcomment')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testcomment,Comments))
    #testing for savinng method
    def test_save_comment(self):
        self.testcomment.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) > 0)
    #testng for deleting method
    def test_delete_comment(self):
        self.testcomment.save_comment()
        self.testcomment.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 1 )

class ImageTestClass(TestCase):
    #set Up method
    def setUp(self):
        self.testimage = Image(image = 'testimage')
    #test  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testimage,Image))
    #testing for saving method
    def test_save_image(self):
        self.testimage.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for deleting method
    def test_delete_image(self):
        self.testimage.save_image()
        self.testimage.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    #testing for update caption
    def test_update_caption(self):
        self.testimage.save_image()
        self.testimage.update_caption()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)