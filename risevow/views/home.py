from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from notes.models.notes import Note
#from notes.models.tag import Tag
from django.contrib.auth.mixins import LoginRequiredMixin
# login_required decorator
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import logout


#from faker import Faker

def HomeView(request):
    template_name = 'risevow\index.html'
    context = {
    "characters": [
                {
                    "name": "Captain Waffles",
                    "species": "Space Cat",
                    "catchphrase": "To the Milky Way and beyond!",
                    "skills": ["Laser eyes", "Zero-gravity purring", "Intergalactic diplomacy"]
                },
                {
                    "name": "Sir Barksalot",
                    "species": "Cybernetic Dog",
                    "catchphrase": "Woof woof... engaged!",
                    "skills": ["Super sniffing", "Fetch at light speed", "Bionic tail wag"]
                },
                {
                    "name": "Professor Quokka",
                    "species": "Mystical Quokka",
                    "catchphrase": "Happiness is the key to the universe!",
                    "skills": ["Quantum physics", "Cheeky grin", "Pocket-sized wisdom"]
                }
            ]
            }
    return render(request, template_name, context)

