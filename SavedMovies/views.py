from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Movie.models import Movie
from Authentication.models import User
from .form import FavoriteMoviesForm, WatchListForm, WatchedForm, UserForm


# Create your views here.

class login_user(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user is not None:
            return HttpResponse('EXISTS')
        else:
            return HttpResponse('User not found')

class register_User(View):
    template = 'registeruser.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template, {'form':form})

class register_Favmovie(View):
    template = 'registration1.html'

    def get(self, request):
        form = FavoriteMoviesForm()
        return render(request, self.template,{'form':form})

    def post(self, request):
        form = FavoriteMoviesForm(request.POST)
        if form.is_valid():
            Favmovie = form.save(commit=False)

            favID = request.POST.get('favoriteID')
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            userID = User.objects.get(pk=user)
            MovieId = Movie.objects.get(pk=movieID)


            Favmovie.favoriteID = favID
            Favmovie.username = userID
            Favmovie.movieID = MovieId

            Favmovie.save()

        return render(request, self.template, {'form':form})


class register_Watchlist(View):
    template = 'registration2.html'

    def get(self, request):
        form = WatchListForm()
        return render(request, self.template,{'form':form})

    def post(self, request):
        form = WatchListForm(request.POST)
        if form.is_valid():
            Watchlist = form.save(commit=False)

            watchlistID = request.POST.get('watchlistID')
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            userID = User.objects.get(pk=user)
            MovieId = Movie.objects.get(pk=movieID)

            Watchlist.watchlistID = watchlistID
            Watchlist.username = userID
            Watchlist.movieID = MovieId

            Watchlist.save()

        return render(request, self.template, {'form': form})


class register_Watched(View):
    template = 'registration3.html'

    def get(self, request):
        form = WatchedForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = WatchedForm(request.POST)
        if form.is_valid():
            Watched = form.save(commit=False)


            user = request.POST.get('user')
            movieID = request.POST.get('movieID')
            datewatched = request.POST.get('date')

            userID = User.objects.get(pk=user)
            MovieId = Movie.objects.get(pk=movieID)

            Watched.date_marked_as_watched = datewatched
            Watched.username = userID
            Watched.movie = MovieId

            Watched.save()

        return render(request, self.template, {'form': form})