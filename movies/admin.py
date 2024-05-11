from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
   list_display =  ('title', 'description','release_date')
   search_fields = ('title',  'description','release_date') 

