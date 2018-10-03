from django.shortcuts import render

# Create your views here.
def instagram(request):
    return render(request, 'instagram.html')


def all_images(request):
    images = Image.objects.all()

    return render(request, "all-images/today-images.html", {"images": images})