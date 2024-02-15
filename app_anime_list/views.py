from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.db.models import Sum

from .models import Anime, AnimeType


def index(request):
    num_anime_types = AnimeType.objects.count()
    num_anime = Anime.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_anime": num_anime,
        "num_anime_types": num_anime_types,
        "num_visits": num_visits + 1
    }

    return render(request, "app_anime_list/index.html", context=context)


class AnimeListView(generic.ListView):
    model = Anime
    template_name = "app_anime_list/anime_list.html"
    context_object_name = "anime_list"
    
    def get_queryset(self):
        return Anime.objects.select_related("type")


class AnimeCreateView(generic.CreateView):
    model = Anime
    template_name = 'app_anime_list/create_anime.html'
    fields = "__all__"
    success_url = reverse_lazy('app_anime_list:anime-list')
