from django.contrib import admin
from django.urls import path, include
from risevow.views import home





urlspatterns = [
    path('', home.HomeView, name="index"),
    path('', include('risevow.urls')),
]