from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from .models import Movies



def index(request):
        return render(request, 'index.html')
def movie(request):
        return render(request, 'movies/movie.html')
def movies(request):
        return render(request, 'movies/movies.html' , {'mov':Movies.objects.all()})

def about(request):
        return render(request , 'index2.html')
