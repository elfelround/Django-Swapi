from django.contrib import admin
from django.urls import path, include
from starwarsapp.views import (
    PeopleListView, test_view, carrusel, FilmCreateView, FilmListView, FilmDelete,
    FilmUpdateView,
    )
from fetcher.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', PeopleListView),
    path('test/', test_view),
    path('create_film/', FilmCreateView.as_view(), name='film-create'),
    path('<int:pk>/update_film/', FilmUpdateView.as_view(), name='film-update'),
    path('list_film/', FilmListView.as_view(), name='film-list'),
    path('<int:pk>/delete_film/', FilmDelete.as_view(), name='film-delete'),
    path('search/', get_data, name='search'),
    path('', carrusel, name='home'),
]
