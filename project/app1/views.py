from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Movie
from .forms import MovieForm
# Create your views here.

class MovieView(View):
    def get(self,request):
        movies = Movie.objects.all()
        context = {
            'movie_lists': movies
        }

        return render(request, "app1/movie.html", context=context)

class Single_Movie_View(View):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            movie = None

        context = {
            'movie': movie
        }

        return render(request, 'app1/mo.html', context)

class AddMovieView(View):
    def get(self, request):
        return render(request, 'app1/add.html')
    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            description = request.POST.get('description')
            year = request.POST.get('year')
            img = request.FILES.get('img')

        if name and description and year and img:
            movie = Movie(
                name=name,
                description=description,
                year=year,
                img=img
            )
            movie.save()
            return redirect('app1:home')
        else:

            return render(request, 'app1/add.html')

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("app1:home")
    return render(request, 'app1/edit.html', {'form': form, 'movie': movie})

def del_movie(request, id):
    if request.method =="POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect("app1:home")
    return render(request, 'app1/delete.html')
