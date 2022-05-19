from re import I
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

class ConcertCreateView(LoginRequiredMixin, CreateView): 
    model = Concert 
    template_name = "concerts/concertslist.html" 
    success_url = reverse_lazy("home") 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)     

def display_concerts(request): 
    url = 'https://api.setlist.fm/rest/1.0/'
    artist_setlist_path = 'artist/b071f9fa-14b0-4217-8e97-eb41da73f598/setlists'
    header = {
    "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
    "Accept": "application/json"
    } 
    params = {
    "p": 1
    }
    concerts_list = []
    setlists = requests.get(f"{url}{artist_setlist_path}", params=params, headers=header).json() 
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

def format_date(date):
    proper_date = date.split("-") 
    #proper_date_list = [MM, DD, YEAR] 
    return proper_date[2] + "-" + proper_date[1] + "-" + proper_date[0]

def log_concert_and_song(request, concertdict):
    if request.method == "POST":
        url = 'https://api.setlist.fm/rest/1.0/'
        setlist_path = f'setlist/{concertdict}'
        header = {
        "x-api-key": "D8tTr14QrM5GLkqKQejjnNX3trT-o_cjW7gL",
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
        list_of_songs_from_api = setlists['sets']['set'][0]['song'] #[{"name": "Shame, Shame, Shame","cover": {},},{"name": "Down the Road Apiece", "cover": { },}]
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
        queryset = Concert.objects.filter(user=self.request.user)
        return queryset

class SongListView(LoginRequiredMixin, ListView):
    model = Song 
    template_name = "concerts/usersonglist.html" 

    def get_queryset(self):
        queryset = Song.objects.filter(user=self.request.user)
        return queryset


class ConcertDeleteView(DeleteView):
    model = Concert
    success_url = reverse_lazy('user_concert_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

 