from django.shortcuts import render
# from musician.models import Musician
from album.models import AlbumModel

def home(request):
    # post = Musician.objects.all()
    post = AlbumModel.objects.all()
    return render(request,'home.html',{'Data':post })
