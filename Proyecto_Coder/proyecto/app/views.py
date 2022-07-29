from urllib import request
from django.shortcuts import render
from app.models import Historias
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def about_me(request):
    return render (request, "app/about_me.html")

class Historias_lista(ListView):
    
    model= Historias
    template_name= "app/historia_lista.html"

