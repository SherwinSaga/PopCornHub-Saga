

from django.db import models

from Authentication.models import *
from Movie.models import Movie


class FavoriteMovies(models.Model):
    favoriteID = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    pass


class WatchList(models.Model):
    watchlistID = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # movieID = Foreign key sa list of movies
    pass


class Watched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_marked_as_watched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Watched"

