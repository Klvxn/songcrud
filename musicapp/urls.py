from django.urls import path

from .views import ArtisteDetail, ArtistesList, SongDetail, SongsList


urlpatterns = [
    path("artistes/", ArtistesList.as_view()),
    path("artistes/<int:pk>/", ArtisteDetail.as_view()),
    path("songs/", SongsList.as_view()),
    path("songs/<int:pk>/", SongDetail.as_view())
]
