from django.urls import path, include
from . import views

urlpatterns = [
     
    path('actors/', views.ActorsCreateView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', views.ActorsDetailView.as_view(), name='actors-detail-view'),
    
]
