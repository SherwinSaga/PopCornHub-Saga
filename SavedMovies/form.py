from django import forms
from .models import Movie
from .models import *
from Authentication.models import *

class FavoriteMoviesForm(forms.ModelForm):

    class Meta:
        model = FavoriteMovies
        fields=['favoriteID', 'user',  'movieID']


class WatchListForm(forms.ModelForm):

    class Meta:
        model = WatchList
        fields=['watchlistID', 'user', 'movieID']


class WatchedForm(forms.ModelForm):

    class Meta:
        model = Watched
        fields=['user', 'movie']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields=['username', 'password', 'first_name', 'last_name', 'email']