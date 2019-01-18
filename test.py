#!/usr/bin/python3

'''Script to get information from https://swapi.co/'''

import requests
import json
import sys

#TODO: Print useful information such as movie titles or names of worlds instead of showing links
#Break up URL to allow for more dynamic searching in the future. Right now, script only handles the people parameter when getting info from the API.

UNDERLINE_LEN = 30

def show(data, index=0):
    '''
        Displays an individual Swapi object.
        data = data retrieved from api
        index = which entry to select. Default is 0 for single item lists.
    '''
    info = data['results'][index]
    print()
    print('-' * UNDERLINE_LEN)
    print("Name : {0}\n{1}".format(data['results'][index]['name'], '-' * UNDERLINE_LEN))
    for k, v in info.items():
        if type(v) is list:
            counter = 0
            print(k, ':')
            for j in v:
                print("\t{0}".format(v[counter]))
                counter += 1
        else: 
            if k != 'name':
                print(k, ':', v)


def show_choices(data):
    '''Shows a list of Swapi objects and prompts users to select an object [integer]'''
    info = data['results']
    counter = 0
    for i in info:
        print("[{0}] {1}".format(counter + 1, data['results'][counter]['name']))
        counter += 1
    print()
    choice = int(input("Which item would you like to view? "))
    try:
        show(data, choice - 1)
    except IndexError as ie:
        print(ie)


def grab():
    '''Main function.'''
    try:
        search = sys.argv[1]
        url = 'https://swapi.co/api/people/?search={0}'.format(search)      #need to divide url to make search process more dynamic
        r = requests.get(url)
        data = json.loads(r.text)
        if data is not None:
            numResults = int(data['count'])
            txt = "results"
            if numResults == 1:
                txt = "result"    
            resText = "{0} {1} found for search parameter '{2}'".format(numResults, txt, search)
            print(resText)
            if numResults == 1:
                show(data)
            else:
                show_choices(data)      
    except Exception as e:
        print(e)

grab()
