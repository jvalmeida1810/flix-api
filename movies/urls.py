from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateView.as_view(), name='movies-create-list'),
     path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movies-detail-view'),
]
