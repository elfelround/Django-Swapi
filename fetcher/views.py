from django.shortcuts import render
import swapi
from starwarsapp.models import Film

# film = Film (title = #models.CharField(max_length=100)
#    episode_id = #models.IntegerField()
#    opening_crawl = #models.TextField(max_length=1000)
#    director = #models.CharField(max_length=100)
#    producer = #models.CharField(max_length=100)
#    release_date = )

# swapi methods https://swapi-python.readthedocs.io/en/latest/readme.html#methods
# Create your views here.
from django.http import HttpResponse
import requests
import json


from django.shortcuts import render
import requests

def search_view(request):
    if request.method == 'POST':
        response = requests.get('https://swapi.co/api/people/?search=r2' #+ request.POST.searchvalue
        )
        searchresponse = response.json()
        return render(request, 'fetcher/search.html', {
            'name': searchresponse['name'],
            'height': searchresponse['height']
        })




def get_data(request):
    #serialized_data = urllib2.urlopen(url).read()
    r = requests.get(‘https://swapi.co/api/people/?search=’ + request.POST)
    data = json.loads(serialized_data)

    html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(data, indent=2)

    return HttpResponse(html)

'''Searching
All resources support a search parameter that filters the set of resources returned.
This allows you to make queries like:

https://swapi.co/api/people/?search=r2

All searches will use case-insensitive partial matches on the set of search
if fields:
To see the set of search fields for each resource, check out the individual
resource documentation. For more information on advanced search terms see here.'''
