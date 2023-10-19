from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Movie.models import Movie
from Authentication.models import User
from .form import SavedMoviesForm

# Create your views here.

def login_view(request):
    return render(request, 'login.html')


class register_Favmovie(View):
    template = 'registration.html'

    def get(self, request):
        form = SavedMoviesForm()
        return render(request, self.template,{'form':form})

    def post(self, request):
        form = SavedMoviesForm(request.POST)
        if form.is_valid():
            Favmovie = form.save(commit=False)

            favID = request.POST.get('favoriteID')
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            username = User.objects.get(pk=user)
            MovieId = Movie.objects.get(pk=movieID)

            Favmovie.username = username
            Favmovie.movieID = MovieId

            Favmovie.save()

        return render(request, self.template, {'form':form})