"""starwars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from starwarsapp.views import testView, PeopleListView, test_view, navbar, carrusel, FilmCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', PeopleListView),
    path('test/', test_view),
    path('navbar/', navbar),
    path('create_film/', FilmCreateView.as_view(), name='film-create'),
#    path('search/', search_view, name='search'),
    path('', carrusel, name='home'),
]
