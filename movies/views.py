from rest_framework import generics
from movies.models import Movie
from movies.serializers import  MovieModelSeriealizer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission

class MovieCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSeriealizer
    
    
    
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSeriealizer