from django.urls import path
from . import views
app_name='SavedMovies'
urlpatterns=[
    path('login/', views.login_view, name='login'),
    path('register/', views.register_Favmovie.as_view(), name='register'),
]

