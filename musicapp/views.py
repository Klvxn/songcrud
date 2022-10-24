from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer


# Create your views here.
class ArtistesList(generics.ListAPIView):

    permission_classes = [AllowAny]
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    lookup_field = "pk"

    
class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [AllowAny]
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    lookup_field = "pk"


class SongsList(generics.ListAPIView):

    permission_classes = [AllowAny]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = "pk"


class SongDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [AllowAny]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = "pk"