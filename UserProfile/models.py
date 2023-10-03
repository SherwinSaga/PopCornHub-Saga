from django.db import models

from Authentication.models import User


# Create your models here.
class UserProfile(models.Model):
    # Kulang pa ang user model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass


class FavoriteMovies(models.Model):
    favoriteID = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # movieID = Foreign key sa list of movies.
    pass


class WatchList(models.Model):
    watchlistID = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # movieID = Foreign key sa list of movies
    pass


class ReviewMade(models.Model):
    # reviewMade =  primary key sa reviewMade nga table.

    """ userID = Maybe I should get the userID  as foreign key for me to know what are the movies or review he had
    made."""

    """" reviewID = for us to know nga unsa nga movie ang ge review ani nga user, 
    kuhaon nako ang foreign key aning reveiwID. """

    """In summary, gamit ang userID og ang reviewID, mahibawan nako sa review nga table if kani nga foreign 
    keys nag review ngadto sa review."""

    pass
