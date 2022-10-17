from rest_framework import generics


from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer


# Create your views here.
class ArtistesList(generics.ListCreateAPIView):

    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class SongsList(generics.ListAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer