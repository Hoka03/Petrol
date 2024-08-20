from django.urls import path
from .views import (
    CarModelListCreateAPIView,
    CarModelRetrieveUpdateDestroyAPIView,
    CarListCreateAPIView,
    CarRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('car-models/', CarModelListCreateAPIView.as_view(), name='car-model-list-create'),
    path('car-models/<int:pk>/', CarModelRetrieveUpdateDestroyAPIView.as_view(), name='car-model-detail'),
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='car-detail'),
]
