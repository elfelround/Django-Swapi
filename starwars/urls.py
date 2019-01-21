#serving files in development
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from starwarsapp.views import (
    PeopleListView,
    home,
    FilmCreateView,
    PeopleCreateView,
    PeopleImageCreateView,
    PeopleImageListView,
    FilmListView,
    PeopleListView,
    FilmDelete,
    FilmUpdateView,
    film_list_search,
    url_logger_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', PeopleListView),
    path('create_film/', FilmCreateView.as_view(), name='film-create'),
    path('create_people/', PeopleCreateView.as_view(), name='people-create'),
    path('create_people_image/', PeopleImageCreateView.as_view(), name='people-image-create'),
    path('list_people_image/', PeopleImageListView.as_view(), name='people-image-list'),
    path('<int:pk>/update_film/', FilmUpdateView.as_view(), name='film-update'),
    path('list_film/', FilmListView.as_view(), name='film-list'),
    path('character_list/', PeopleListView.as_view(), name='people-list'),
    path('<int:pk>/delete_film/', FilmDelete.as_view(), name='film-delete'),
    path('search/', film_list_search, name='search'),
    path('url-log/', url_logger_view, name='url-logger'),
    path('', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
