from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name= 'reviews')
    stars = models.IntegerField(blank=True, null=True,validators= [
        MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas.'),
        MaxValueValidator(5, 'A avaliação não pode superior a 5 estrelas.') 
    ])
                                 
    comment = models.TextField(max_length=2500, blank=True, null=True)
    
    def __str__(self):
        return str(self.movie)    