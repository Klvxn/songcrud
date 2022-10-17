from django.urls import path

from .views import ArtistesList, SongDetail, SongsList


urlpatterns = [
    path("artistes/", ArtistesList.as_view()),
    path("songs/", SongsList.as_view()),
    path("songs/<int:pk>/", SongDetail.as_view())
]
