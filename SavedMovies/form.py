from django import forms
from .models import Movie
from .models import *
from Authentication.models import *

class SavedMoviesForm(forms.ModelForm):
    #favoriteID = forms.IntegerField(widget=forms.TextInput)
    #user = forms.CharField(widget=forms.TextInput)
    #movie = forms.CharField(widget=forms.TextInput)
    #movieId = forms.CharField(widget=forms.TextInput)
    #watchlistID = forms.IntegerField(widget=forms.TextInput)
    #dateMarkedAsWatched = forms.DateTimeField(widget=forms.TextInput)

    class Meta:
        model = FavoriteMovies
        fields=['favoriteID', 'user',  'movieID']



