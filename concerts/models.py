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
    user = models.ForeignKey(USER_MODEL, related_name="concerts", on_delete=models.CASCADE, null=True) 
    song = models.ManyToManyField("Song", blank=True, null=True)

    def __str__(self): 
        return str(self.concertid) + " " + str(self.venue) + " " + str(self.date) 

class Song(models.Model): 
    name = models.CharField(max_length = 100, null=True) 
    user = models.ForeignKey(USER_MODEL, related_name="songs", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# class ConcertTest(models.Model):
#     venue = models.CharField(max_length=200, null=True)
#     concertid = models.CharField(max_length = 200, null=False, default='didnotsaveproperly', primary_key = True) 
#     date = models.DateField(null=True) 
#     city = models.CharField(max_length=100, null=True)
#     country = models.CharField(max_length=200, null=True)
#     user = models.ForeignKey(USER_MODEL, related_name="testconcerts", on_delete=models.CASCADE, null=True) 
#     song = models.ManyToManyField("SongTest", blank=True, null=True)

#     def __str__(self):
#         return str(self.concertid) + " " + str(self.venue) + " " + str(self.date) 

# class SongTest(models.Model): 
#     name = models.CharField(max_length = 100, null=True) 
#     user = models.ForeignKey(USER_MODEL, related_name="tests", on_delete=models.CASCADE, null=True)
    

#     def __str__(self):
#         return self.name