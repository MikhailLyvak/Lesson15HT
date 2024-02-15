from django.urls import path

from .views import (
    index,
    AnimeListView,
    AnimeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("animes/", AnimeListView.as_view(), name="anime-list"),
    path("animes/create/", AnimeCreateView.as_view(), name="anime-create"),
]

app_name = "app_anime_list"