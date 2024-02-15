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
    
    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        
        context["total_amount"] = Anime.objects.count()
        
        return context


class AnimeCreateView(generic.CreateView):
    model = Anime
    template_name = 'app_anime_list/create_anime.html'
    fields = ["name", "description", "episodes", "type", "url"]
    success_url = reverse_lazy('app_anime_list:anime-list')

    def form_valid(self, form):
        anime = form.save(commit=False)

        if anime.type.name == "Fantasy":
            anime.real_rating = 100
        else:
            anime.real_rating = None

        anime.save()

        return super().form_valid(form)
    

class AnimeUpdateView(generic.UpdateView):
    model = Anime
    template_name = 'app_anime_list/update_anime.html'
    fields = ["name", "description", "episodes", "my_episode", "my_rating", "url"]
    success_url = reverse_lazy('app_anime_list:anime-list')
    

class AnimeDetailView(generic.DetailView):
    model = Anime
    template_name = "app_anime_list/anime_detail.html"
    context_object_name = "anime"
    
    def get_queryset(self):
        return Anime.objects.select_related("type")


def delete_anime(request, pk):
    anime = Anime.objects.get(pk=pk)
    anime.delete()
    return redirect(reverse("app_anime_list:anime-list"))    


def mark_item_as_watched(request, pk):
    item = Anime.objects.get(pk=pk)
    item.is_watched = True
    item.watched_date = datetime.date.today()
    item.save()
    return redirect(reverse("app_anime_list:anime-list"))