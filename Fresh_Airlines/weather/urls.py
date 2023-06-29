from django.urls import path
from .views import weather_search

urlpatterns = [
    path('search/', weather_search, name='search weather'),
]
