from django.db import models
# import models from other apps

# Create your models here.
from Authentication.models import User
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"
