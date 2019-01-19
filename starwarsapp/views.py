from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import People

from django.views.generic import (
    ListView,
    CreateView
)

from .forms import FilmModelForm, SearchForm
from .models import Film

class FilmCreateView(CreateView):
    template_name = "starwarsapp/film/create.html"
    form_class = FilmModelForm
    queryset = Film.objects.all()

def my_view(request):
    search_form = SearchForm(request.POST or None, initial={'name': 'R2'})

    if request.method == 'POST':
        if search_form.is_valid():
           urlquery = 'https://swapi.co/api/people/?search='

    return render(request, 'search-form.html', {'search_form': search_form})


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
