from django.urls import path

from .views import (
    index,
    mark_item_as_watched,
    delete_anime,
    AnimeListView,
    AnimeCreateView,
    AnimeUpdateView,
    AnimeDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("animes/", AnimeListView.as_view(), name="anime-list"),
    path("animes/create/", AnimeCreateView.as_view(), name="anime-create"),
    path("animes/<int:pk>/update/", AnimeUpdateView.as_view(), name="anime-update"),
    path("animes/<int:pk>/detail/", AnimeDetailView.as_view(), name="anime-detail"),
    path("animes/<int:pk>/mark_as_watched/", mark_item_as_watched, name="mark-as-watched"),
    path("animes/<int:pk>/delete/", delete_anime, name="anime-delete")
]

app_name = "app_anime_list"