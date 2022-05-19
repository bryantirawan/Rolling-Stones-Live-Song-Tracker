from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.display_concerts, name="choose_concerts"),
    path('add/<str:concertdict>/', views.log_concert_and_song, name='concert_add'),
    path('userconcerts/', views.ConcertListView.as_view(), name='user_concert_list'),
    path('<int:pk>/delete/', views.ConcertDeleteView.as_view(), name='delete_concert'),
    path('usersonglist/', views.SongListView.as_view(), name='user_song_list'),
]
