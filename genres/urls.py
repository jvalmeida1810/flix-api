from django.urls import path
from . import views 

urlpatterns = [
    path('genres/', views.GenresCreateView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view() , name='genres-detail-view'),
    
    
]
