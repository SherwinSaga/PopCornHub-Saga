from django.db import models
# import models from other apps

# Create your models here.

#temporary model
class User(models.Model):
    # Add any additional user attributes here
    username = models.CharField(max_length=20)
    pass

#temporary model
class Movie(models.Model):
    # Movie attributes
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"
