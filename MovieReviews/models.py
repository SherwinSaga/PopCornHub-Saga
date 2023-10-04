from django.db import models
# import models from other apps

# Create your models here.
from Authentication.models import User
from Movie.models import Movie


class Review(models.Model):
    reviewID = models.CharField(max_length=20, primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
