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

def display_concerts_for_page(request, p, range_min, range_max, sleep): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
     # "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "x-api-key": "1Lw-KTV9OFozLe7JpUeAyOdJHJH9HeVWNn2B",
    "Accept": "application/json"
    } 
    params = {
        "p": p
        }
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json()
    
    x = range_min
    for x in range(range_min, range_max): ##########
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
            time.sleep(sleep)
            page_setlist_json = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
            breakpoint()
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


def display_pageone_concerts(request): 
    return display_concerts_for_page(request, 1, 2, 11, .5)
def display_pagetwo_concerts(request): 
    return display_concerts_for_page(request, 11, 12, 21, .5)
def display_pagethree_concerts(request): 
    return display_concerts_for_page(request, 21, 22, 31, .5)
def display_pagefour_concerts(request): 
    return display_concerts_for_page(request, 31, 31, 41, .5)
def display_pagefive_concerts(request): 
    return display_concerts_for_page(request, 41, 42, 51, .5)
def display_pagesix_concerts(request): 
    return display_concerts_for_page(request, 51, 52, 61, .5)
def display_pageseven_concerts(request): 
    return display_concerts_for_page(request, 61, 62, 71, .5)
def display_pageeight_concerts(request): 
    return display_concerts_for_page(request, 71, 72, 81, .5)
def display_pagenine_concerts(request): 
    return display_concerts_for_page(request, 81, 82, 91, .5)
def display_pageten_concerts(request): 
    # return display_concerts_for_page(request, 91, 92, 110, .5)
    
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
        try: 
            Concert_save = Concert.objects.get(concertid = concertdict['id']) #check to see if Concert exists already 
        except: 
            Concert_save = Concert(
                concertid=concertdict['id'], 
                date=concertdict['eventDate'], 
                venue=concertdict['venue'], 
                city=concertdict['city'], 
                country=concertdict['country'], 
                )
            
        Concert_save.save() #save instance to Concert model 
        Concert_save.user.add(request.user) #assign user to Concert just saved (many to many needs to be created before assigned)
            
        user_concert_list.append(concertdict)  
        songdict = {} # {concertid: [song1, song2, etc.]} #not needed for saving song name but in case I need to reference 
        
        
        
        #grabbing songs from a concert to save 
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
                Song_save = Song.objects.get(name=song_name) #check to see if a song exists already 
            except: 
                Song_save = Song(
                    name=song_name,
                )
                
            Song_save.save() #save song instance to Song model 
            Song_save.user.add(request.user) #many to many relationship with song and user 
            Concert_save.song.add(Song_save) #many to many relationship with song to Concert 

            final_list.append(song['name']) #not really needed but made just in case needed to reference 
            songdict[concert_id_to_generate_songs] = final_list #not really needed but made just in case needed to reference 
        
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

 