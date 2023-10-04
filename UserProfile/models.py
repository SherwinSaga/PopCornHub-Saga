from django.db import models

from Authentication.models import User
from MovieReviews.models import Review
from SavedMovies.models import FavoriteMovies
from SavedMovies.models import WatchList
from SavedMovies.models import Watched


# Create your models here.
class Profile(models.Model):
    # Kulang pa ang user model.
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    favoriteID = models.ForeignKey(FavoriteMovies, on_delete=models.CASCADE)
    watchlistID = models.ForeignKey(WatchList, on_delete=models.CASCADE)
    watched = models.ForeignKey(Watched, on_delete=models.CASCADE)
    reviewID = models.ForeignKey(Review, on_delete=models.CASCADE)
