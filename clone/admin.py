from django.contrib import admin
from .models import Image,Comments,Profile

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
