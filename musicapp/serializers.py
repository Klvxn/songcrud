from rest_framework import serializers

from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artiste
        fields = ["first_name", "last_name", "age"]


class LyricSerializer(serializers.ModelSerializer):

    song_id = serializers.SerializerMethodField()
    class Meta:
        model = Lyric
        fields = ["song_id", "lyric"]

    def get_song_id(self, obj):
        return obj.song_id.title


class SongSerializer(serializers.ModelSerializer):

    artiste_id = ArtisteSerializer()
    lyric = LyricSerializer(required=False)
    class Meta:
        model = Song
        fields = ["title", "date_released", "artiste_id", "lyric", "likes"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.date_released = validated_data.get("date_released", instance.date_released)
        return instance
