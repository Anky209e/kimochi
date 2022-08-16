from curses.ascii import SO
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Song

@login_required
def home(request):
    songs = Song.objects.all()
    
    context = {
        "names":songs
    }

    return render(request,"player/home.html",context)