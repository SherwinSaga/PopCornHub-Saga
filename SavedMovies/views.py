from django.contrib.auth import authenticate, login
from django.db import connection
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
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            userID = User.objects.get(username=user).pk
            MovieId = Movie.objects.get(MovieID=movieID).pk

            cursor = connection.cursor()
            args = [MovieId,userID]
            cursor.callproc('addToFavorite', args)
            cursor.close()

        return render(request, self.template, {'form':form})


class register_Watchlist(View):
    template = 'registration2.html'

    def get(self, request):
        form = WatchListForm()
        return render(request, self.template,{'form':form})

    def post(self, request):
        form = WatchListForm(request.POST)
        if form.is_valid():
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            userID = User.objects.get(username=user).pk
            MovieId = Movie.objects.get(MovieID=movieID).pk

            cursor = connection.cursor()
            args = [MovieId, userID]
            cursor.callproc('addToWatchlist', args)
            cursor.close()

        return render(request, self.template, {'form': form})


class register_Watched(View):
    template = 'registration3.html'

    def get(self, request):
        form = WatchedForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = WatchedForm(request.POST)
        if form.is_valid():
            user = request.POST.get('user')
            movieID = request.POST.get('movieID')

            userID = User.objects.get(username=user).pk
            MovieId = Movie.objects.get(MovieID=movieID).pk

            cursor = connection.cursor()
            args = [MovieId, userID]
            cursor.callproc('markWatched', args)
            cursor.close()

        return render(request, self.template, {'form': form})