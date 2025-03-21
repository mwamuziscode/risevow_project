from django.contrib import admin
from django.urls import path


from .views import home


urlspatterns = [
    path('', home.HomeViews.as_view(), name="index")
]