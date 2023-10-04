from django.shortcuts import render, redirect
from Authentication.models import User


# Create your views here.

def log_in(request):
    return render(request, "login.html")


def sign_up(request):
    return render(request, 'signup.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')

        user = User(username=username, password=password,
                    first_name=first_name,
                    last_name=last_name, email=email)

        user.save()

    return render(request, 'login.html')
