from rest_framework import serializers
from .models import Director, Genre, Movie, Showtime


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        director_data = validated_data.pop('director')
        director, _ = Director.objects.get_or_create(**director_data)
        genre_data = validated_data.pop('genre')
        genre, _ = Genre.objects.get_or_create(**genre_data)
        movie = Movie.objects.create(director=director, genre=genre, **validated_data)
        return movie


class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Showtime
        fields = '__all__'