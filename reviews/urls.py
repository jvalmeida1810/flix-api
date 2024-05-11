from django.urls import path
from . import views
urlpatterns = [
    path('reviews/', views.ReviewCreateView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='reviews-detail-view'),
]
