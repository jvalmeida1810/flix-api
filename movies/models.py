from django.db import models
from actors.models import Actor
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name= 'movies')
    description = models.TextField(max_length=2500)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    def __str__(self):
      return self.title        
