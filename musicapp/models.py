from django.db import models


# Create your models here.
class Artiste(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.first_name

    
class Song(models.Model):
    
    title = models.CharField(max_length=100)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Lyric(models.Model):
    
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

