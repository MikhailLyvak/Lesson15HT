from django.db import models

class AnimeType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}"
    

class Anime(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(AnimeType, on_delete=models.CASCADE, null=True, blank=True)
    episodes = models.PositiveIntegerField(null=True, blank=True)
    my_episode = models.PositiveIntegerField(null=True, blank=True)
    my_rating = models.PositiveIntegerField(null=True, blank=True)

    
    def __str__(self) -> str:
        return f"{self.name} Rating: {self.my_rating} {self.type} | {self.my_episode}/{self.episodes}"
