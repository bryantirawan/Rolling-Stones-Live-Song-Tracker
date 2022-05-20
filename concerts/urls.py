from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.display_pageone_concerts, name="choose_concerts"), 
    path("concertslistpage2.html", views.display_pagetwo_concerts, name="concerts_second_page"), 
    path("concertslistpage3.html", views.display_pagethree_concerts, name="concerts_third_page"), 
    path("concertslistpage4.html", views.display_pagefour_concerts, name="concerts_fourth_page"), 
    path("concertslistpage5.html", views.display_pagefive_concerts, name="concerts_fifth_page"), 
    path("concertslistpage6.html", views.display_pagesix_concerts, name="concerts_sixth_page"), 
    path("concertslistpage7.html", views.display_pageseven_concerts, name="concerts_seventh_page"), 
    path("concertslistpage8.html", views.display_pageeight_concerts, name="concerts_eighth_page"), 
    path("concertslistpage9.html", views.display_pagenine_concerts, name="concerts_ninth_page"), 
    path("concertslistpage10.html", views.display_pageten_concerts, name="concerts_tenth_page"), 

    path('add/<str:concertdict>/', views.log_concert_and_song, name='concert_add'),
    path('userconcerts/', views.ConcertListView.as_view(), name='user_concert_list'),
    path('<int:pk>/delete/', views.ConcertDeleteView.as_view(), name='delete_concert'),
    path('usersonglist/', views.SongListView.as_view(), name='user_song_list'),
    path('deleteuserconcertandsongs/', views.delete_all_concerts_and_songs, name='delete_user_concerts_and_songs'),
    
]
