from django.db import models
from django.conf import settings
from django.shortcuts import render  

USER_MODEL = settings.AUTH_USER_MODEL 


class Concert(models.Model):
    venue = models.CharField(max_length=200, null=True)
    concertid = models.CharField(max_length = 200, null=False, default='didnotsaveproperly') 
    date = models.DateField(null=True) 
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=200, null=True)
    user = models.ManyToManyField(USER_MODEL, related_name="concerts", null=True) 
    song = models.ManyToManyField("Song", blank=True, null=True)

    def __str__(self): 
        return str(self.concertid) + " " + str(self.venue) + " " + str(self.date) 

class Song(models.Model): 
    name = models.CharField(max_length = 100, null=True) 
    user = models.ManyToManyField(USER_MODEL, related_name="songs", null=True)

    def __str__(self):
        return self.name

# class User 
#username, pw, counter per song? 
    #def count song method 


