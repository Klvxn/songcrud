from rest_framework import serializers

from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artiste
        fields = ["first_name", "last_name", "age"]


class LyricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lyric
        fields = ["content"]


class SongSerializer(serializers.ModelSerializer):

    artiste_id = ArtisteSerializer()
    lyric_set = LyricSerializer(many=True, required=False)

    class Meta:
        model = Song
        fields = ["title", "date_released", "likes", "artiste_id", "lyric_set"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.date_released = validated_data.get("date_released", instance.date_released)
        return instance
