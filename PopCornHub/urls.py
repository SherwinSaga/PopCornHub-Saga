from django.urls import include, path
from Authentication import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup')
]
