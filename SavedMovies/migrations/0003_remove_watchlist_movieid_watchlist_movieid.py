# Generated by Django 4.2.5 on 2023-10-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_alter_movie_movieid'),
        ('SavedMovies', '0002_watchlist_movieid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='movieId',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='movieID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.movie'),
        ),
    ]
