from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Showtime(models.Model):
    date = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
