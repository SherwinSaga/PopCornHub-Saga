from django.contrib import admin
from django.urls import include, path
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('login/register', views.register, name='register'),
]
