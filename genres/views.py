from rest_framework import generics 
from genres.models import Genre
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermission

   
class GenresCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
