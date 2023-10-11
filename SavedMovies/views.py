from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import SavedMoviesForm

# Create your views here.

def login_view(request):
    return render(request, 'login.html')


class register_Favmovie(View):
    template = 'registration.html'

    def get(self, request):
        form = SavedMoviesForm()
        return render(request, self.template,{'form':form})