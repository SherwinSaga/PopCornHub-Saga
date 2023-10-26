from django.urls import path
from . import views
app_name='SavedMovies'
urlpatterns=[
    path('login/', views.login_user.as_view(), name='login'),
    path('register0/', views.register_User.as_view(), name='register0'),
    path('register1/', views.register_Favmovie.as_view(), name='register1'),
    path('register2/', views.register_Watchlist.as_view(), name='register2'),
    path('register3/', views.register_Watched.as_view(), name='register3'),
]

