from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music, name='music'),
    path('music/<int:song_id>/', views.detail, name='detail'),
    path('', views.homepage, name='homepage'),
    path('recent/', views.recent, name='recent'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlist/<int:playlist_id>/', views.detail_playlist, name='detail_playlist'),
]