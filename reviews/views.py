from rest_framework import  generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission

class ReviewCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer