from django import forms
from .models import Movie
from .models import *
from Authentication.models import *

class FavoriteMoviesForm(forms.ModelForm):
    #favoriteID = forms.IntegerField(widget=forms.TextInput)
    #user = forms.CharField(widget=forms.TextInput)
    #movie = forms.CharField(widget=forms.TextInput)
    #movieId = forms.CharField(widget=forms.TextInput)
    #watchlistID = forms.IntegerField(widget=forms.TextInput)
    #dateMarkedAsWatched = forms.DateTimeField(widget=forms.TextInput)

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