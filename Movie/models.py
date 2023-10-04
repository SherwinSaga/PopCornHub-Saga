from django.db import models

# Create your models here.
class Movie(models.Model):
    MovieID = models.CharField(max_length=20, primary_key=True)
    MovieTitle = models.TextField()
    ReleaseDate = models.DateField()
    Genre = models.CharField(max_length=100)
    Description = models.TextField()
    Rating = models.FloatField()
    RunTime = models.IntegerField()

    def __str__(self):
        return self.MovieTitle