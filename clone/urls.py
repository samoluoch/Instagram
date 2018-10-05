from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^instagram/$',views.instagram,name = 'instagram'),
    # url(r'^$',views.all_images,name = 'image'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_image,name = 'pastImages'),
    url(r'^search/', views.search_profile, name='search_profile'),
    # url(r'^image/(\d+)',views.image,name = 'specificImage'),
    # url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^user/', views.profile, name='profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^edit/',views.edit_profile, name='edit_profile'),
    url(r'^$',views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)