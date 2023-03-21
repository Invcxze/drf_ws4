"""drf_ws4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import DirectorList, DirectorDetail, GenreList, GenreDetail, MovieList, MovieDetail, ShowtimeList, ShowtimeDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directors/', DirectorList.as_view(), name='director_list'),
    path('directors/<int:pk>/', DirectorDetail.as_view(), name='director_detail'),
    path('genres/', GenreList.as_view(), name='genre_list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre_detail'),
    path('movies/', MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('showtimes/', ShowtimeList.as_view(), name='schedule_list'),
    path('showtimes/<int:pk>/', ShowtimeDetail.as_view(), name='schedule_detail'),

]
