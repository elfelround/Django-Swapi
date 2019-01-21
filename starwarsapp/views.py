from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q #complex lookpus

from .models import (
    People,
    Planet,
    Film,
    Starship,
    Vehicle,
    Species,
    Hero,
    PeopleImage,
)

from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)

from .forms import FilmModelForm, SearchForm


class FilmCreateView(CreateView):
    template_name = "starwarsapp/film/create.html"
    form_class = FilmModelForm
    queryset = Film.objects.all()
    success_url = reverse_lazy('home')

    def get_absolute_url(self):
        return self.reverse('home')


class FilmUpdateView(UpdateView):
    template_name = "starwarsapp/film/update.html"
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('home')


class FilmListView(ListView):
    model = Film
    queryset = Film.objects.all()
    context_object_name = 'films'
    template_name = 'starwarsapp/film/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def film_list_search(request):
    # vs request.GET["q"]
    query = request.GET.get("q", None)  # None case no query
    qs = Film.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(opening_crawl__icontains=query) |
            Q(director__icontains=query) |
            Q(producer__icontains=query) |
            Q(release_date__icontains=query)
            )

        context = {
            'films': qs,
        }
        template = 'starwarsapp/film/list.html'
        return render(request, template, context)



class FilmDelete(DeleteView):
    model = Film
    template_name = 'starwarsapp/film/delete.html'

    def get_success_url(self):
        return reverse_lazy('film-list')
        # Assuming there is a ForeignKey from Comment to Post in your model


def my_view(request):
    search_form = SearchForm(request.POST or None, initial={'name': 'R2'})

    if request.method == 'POST':
        if search_form.is_valid():
           urlquery = 'https://swapi.co/api/people/?search='

    return render(request, 'search-form.html', {'search_form': search_form})


def test_view(request):
    return render(request, "starwarsapp/test.html")


def Home(request):
    return render(request, "starwarsapp/carrusel.html")


class PeopleListView(ListView):
    queryset = People.objects.all()
    template_name = 'starwarsapp/people/list.html'

