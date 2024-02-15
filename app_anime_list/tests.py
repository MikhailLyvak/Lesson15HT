from django.test import TestCase, Client
from django.urls import reverse
from .models import Anime, AnimeType
from django.conf import settings

settings.DEBUG = True

class MoreAnimeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.animeType = AnimeType.objects.create(name='Fantasy')

    def test_anime_create_view(self):
        response = self.client.post(reverse('app_anime_list:anime-create'), {
            'name': 'New Anime',
            'description': 'New Description',
            'type': self.animeType.pk,
            'episodes': 24,
            'my_episode': 10,
            'my_rating': 9,
            'url': 'http://newexample.com',
            'is_watched': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Anime.objects.count(), 1)

        anime = Anime.objects.get(name='New Anime')
        self.assertEqual(anime.real_rating, 100)

    def test_anime_update_view(self):
        anime = Anime.objects.create(
            name='Existing Anime',
            description='Existing Description',
            type=self.animeType,
            episodes=12,
            my_episode=5,
            my_rating=8,
            real_rating=80,
            url='http://example.com',
            is_watched=False
        )
        response = self.client.post(reverse('app_anime_list:anime-update', kwargs={'pk': anime.pk}), {
            'name': 'Updated Anime',
            'description': 'Updated Description',
            'type': self.animeType.pk,
            'episodes': 24,
            'my_episode': 10,
            'my_rating': 9,
            'url': 'http://updatedexample.com',
            'is_watched': False
        })
        self.assertEqual(response.status_code, 302)
        anime.refresh_from_db()
        self.assertEqual(anime.name, 'Updated Anime')

    def test_anime_detail_view(self):
        anime = Anime.objects.create(
            name='Detail Anime',
            description='Detail Description',
            type=self.animeType,
            episodes=12,
            my_episode=5,
            my_rating=8,
            real_rating=80,
            url='http://example.com',
            is_watched=False
        )
        response = self.client.get(reverse('app_anime_list:anime-detail', kwargs={'pk': anime.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail Anime')

    def test_delete_anime_view(self):
        anime = Anime.objects.create(
            name='Anime to Delete',
            description='Description to Delete',
            type=self.animeType,
            episodes=12,
            my_episode=5,
            my_rating=8,
            real_rating=80,
            url='http://example.com',
            is_watched=False
        )
        response = self.client.get(reverse('app_anime_list:anime-delete', kwargs={'pk': anime.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Anime.objects.count(), 0)

    def test_mark_item_as_watched_view(self):
        anime = Anime.objects.create(
            name='Anime to Mark as Watched',
            description='Description to Mark as Watched',
            type=self.animeType,
            episodes=12,
            my_episode=5,
            my_rating=8,
            real_rating=80,
            url='http://example.com',
            is_watched=False
        )
        response = self.client.get(reverse('app_anime_list:mark-as-watched', kwargs={'pk': anime.pk}))
        anime.refresh_from_db()
        self.assertTrue(anime.is_watched)
        

class AnimeCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.animeType = AnimeType.objects.create(name='Fantasy')

    def test_form_valid_with_fantasy_type(self):
        form_data = {
            'name': 'New Fantasy Anime',
            'description': 'Description of a fantasy anime',
            'type': self.animeType.pk,
            'episodes': 12,
            'my_episode': 5,
            'my_rating': 8,
            'url': 'http://example.com',
            'is_watched': False
        }

        response = self.client.post(reverse('app_anime_list:anime-create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        created_anime = Anime.objects.get(name='New Fantasy Anime')
        self.assertEqual(created_anime.real_rating, 100)
        
    def test_form_valid_with_non_fantasy_type(self):
        non_fantasy_type = AnimeType.objects.create(name='Non-Fantasy')
        form_data = {
            'name': 'New Non-Fantasy Anime',
            'description': 'Description of a non-fantasy anime',
            'type': non_fantasy_type.pk,
            'episodes': 12,
            'my_episode': 5,
            'my_rating': 8,
            'url': 'http://example.com',
            'is_watched': False
        }
        # Sending a POST request to the create view
        response = self.client.post(reverse('app_anime_list:anime-create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        created_anime = Anime.objects.get(name='New Non-Fantasy Anime')
        self.assertIsNone(created_anime.real_rating)
