from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(User)
admin.site.register(FavoriteMovies)
admin.site.register(WatchList)
admin.site.register(Watched)
