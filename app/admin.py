from django.contrib import admin

from app.models import Director, Genre, Movie, Showtime

# Register your models here.
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Showtime)