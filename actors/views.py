from rest_framework import generics
from actors.models import Actor
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermission

class ActorsCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer    
