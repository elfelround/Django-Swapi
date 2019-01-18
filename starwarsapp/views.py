from django.shortcuts import render, get_object_or_404
from .models import Film
from django.views.generic import ListView
from django.http import HttpResponse
from .models import People
from django.shortcuts import render

def testView(request):
    return HttpResponse('Star Wars')

def test_view(request):
    return render(request, "starwarsapp/test.html")

def navbar(request):
    return render(request, "starwarsapp/navbartest.html")

def carrusel(request):
    return render(request, "starwarsapp/carrusel.html")

class PeopleListView(ListView):
    queryset = People.objects.all()
    template_name = 'starwarsapp/people/list.html'

class FilmListView(ListView):
#    queryset = Film.objects.all()
    context_object_name = 'films'
    template_name = 'starwarsapp/film/list.html'

# Create your views here.
