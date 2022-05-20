from re import I, X
from django.shortcuts import redirect, render 
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import Concert, Song
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
import requests 
import time 

class ConcertCreateView(LoginRequiredMixin, CreateView): 
    model = Concert 
    template_name = "concerts/concertslist.html" 
    success_url = reverse_lazy("home") 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)     

def display_pageone_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 1
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 2
    for x in range (2, 11): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslist.html', context) 
def display_pagetwo_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 11
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 12
    for x in range (12, 21): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage2.html', context) 
def display_pagethree_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 21
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 22
    for x in range (22, 31): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage3.html', context) 
def display_pagefour_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 31
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 32
    for x in range (31, 41): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.4)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage4.html', context) 
def display_pagefive_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 41
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 42
    for x in range (42, 51): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage5.html', context) 
def display_pagesix_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 51
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 52
    for x in range (52, 61): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage6.html', context) 
def display_pageseven_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 61
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 62
    for x in range (62, 71): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage7.html', context) 
def display_pageeight_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 71
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 72
    for x in range (72, 81): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.4)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage8.html', context) 
def display_pagenine_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 81
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 82
    for x in range (82, 91): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        if page_setlist_json.get('setlist') == None: 
            time.sleep(0.5)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
        page_setlist = page_setlist_json['setlist'] 
        
        setlists['setlist'].extend(page_setlist) 
        x += 1 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage9.html', context) 
def display_pageten_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": 91
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = 92
    for x in range (92, 110): 
        url = 'https://api.setlist.fm/rest/1.0/'
        artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
        header = {
        # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
            "p": x
            }
        try: 
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
            if page_setlist_json.get('setlist') == None: 
                time.sleep(0.5)
                page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
                
            page_setlist = page_setlist_json['setlist'] 
            
            setlists['setlist'].extend(page_setlist) 
            x += 1 
        except: 
            break 

    concerts_list = []
    i = 0 
    for i in range(0, len(setlists['setlist'])): 
        concertdict = {}
        concertdict['venue'] = setlists['setlist'][i]['venue']['name']
        concertdict['eventDate'] = setlists['setlist'][i]['eventDate']
        concertdict['city'] = setlists['setlist'][i]['venue']['city']['name']
        concertdict['country'] = setlists['setlist'][i]['venue']['city']['country']['name']
        concertdict['id'] = setlists['setlist'][i]['id']
        try: 
            concertdict['specialinfo'] = setlists['setlist'][i]['info']
        except: 
            pass
        concerts_list.append(concertdict)
        i = i + 1 
    context = {
        "setlists" : concerts_list,
        }

    return render(request, 'concerts/concertslistpage10.html', context) 

def format_date(date):
    proper_date = date.split("-") 
    #proper_date_list = [MM, DD, YEAR] 
    return proper_date[2] + "-" + proper_date[1] + "-" + proper_date[0]


def log_concert_and_song(request, concertdict):
    if request.method == "POST":
        url = 'https://api.setlist.fm/rest/1.0/'
        setlist_path = f'setlist/{concertdict}'
        header = {
         # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
        "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
        "Accept": "application/json"
        } 
        params = {
        "p": 1
        }
        
        setlists = requests.get(f"{url}{setlist_path}", params=params, headers=header).json() 
        
        concertdict = {} 
        user_concert_list = []
        concertdict['venue'] = setlists['venue']['name']
        concertdict['eventDate'] = format_date(setlists['eventDate'])
        concertdict['city'] = setlists['venue']['city']['name']
        concertdict['country'] = setlists['venue']['city']['country']['name']
        concertdict['id'] = setlists['id'] 
        concert_id_to_generate_songs = concertdict['id']
        Concert_save = Concert(
            concertid=concertdict['id'], 
            date=concertdict['eventDate'], 
            venue=concertdict['venue'], 
            city=concertdict['city'], 
            country=concertdict['country'], 
            user = request.user
            )
        
        Concert_save.save() 
        user_concert_list.append(concertdict)  

        songdict = {} # {concertid: [song1, song2, etc.]} #not needed for saving song name but in case I need to reference 
        list_of_songs_from_api = []
        try: 
            list_of_songs_from_api = setlists['sets']['set'][0]['song'] #[{"name": "Shame, Shame, Shame","cover": {},},{"name": "Down the Road Apiece", "cover": { },}]
        
            list_of_encores_from_api = setlists['sets']['set'][1]['song'] 
            list_of_songs_from_api.extend(list_of_encores_from_api)
            list_of_encores_from_api = setlists['sets']['set'][2]['song'] 
            list_of_songs_from_api.extend(list_of_encores_from_api)
            list_of_encores_from_api = setlists['sets']['set'][3]['song'] 
            list_of_songs_from_api.extend(list_of_encores_from_api)
            list_of_encores_from_api = setlists['sets']['set'][4]['song'] 
            list_of_songs_from_api.extend(list_of_encores_from_api)
            list_of_encores_from_api = setlists['sets']['set'][5]['song'] 
            list_of_songs_from_api.extend(list_of_encores_from_api)
        except: 
            pass
        final_list = []
        
        for song in list_of_songs_from_api: #song = {"name": "Shame, Shame, Shame","cover": {},}
            song_name = song['name'] 
            try: 
                Song_save = Song.objects.get(name=song_name, user=request.user) 
            except: 
                Song_save = Song(
                    name=song_name,
                    user=request.user
                )
                Song_save.save() 
            
            Concert_save.song.add(Song_save) 

            final_list.append(song['name'])
            songdict[concert_id_to_generate_songs] = final_list 
        
        return redirect("user_concert_list")
    else:
        return render(request, 'concerts/concertslist.html')


class ConcertListView(LoginRequiredMixin, ListView):
    model = Concert 
    template_name = "concerts/userconcerts.html" 
    

    def get_queryset(self):
        queryset = Concert.objects.filter(user=self.request.user).order_by('-date')
        return queryset


class SongListView(LoginRequiredMixin, ListView):
    model = Song 
    template_name = "concerts/usersonglist.html" 

    def get_queryset(self):
        queryset = Song.objects.filter(user=self.request.user).order_by('name')
        return queryset


class ConcertDeleteView(DeleteView):
    model = Concert
    success_url = reverse_lazy('user_concert_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


def delete_all_concerts_and_songs(request):
    Concert.objects.filter(user=request.user).delete()
    Song.objects.filter(user=request.user).delete()
    return redirect("user_concert_list")

 