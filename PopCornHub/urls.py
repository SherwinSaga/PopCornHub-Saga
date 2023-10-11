from django.contrib import admin
from django.urls import path, include

from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/register', views.register, name='register'),
    path('SavedMovies/', include('SavedMovies.urls'))
]