from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView,   DetailView, ListView, UpdateView
)

from .models import Joke

# Joke Create View
class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

# Joke Delete View
class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

# Joke Detail View
class JokeDetailView(DetailView):
    model = Joke

# Joke List View
class JokeListView(ListView):
    model = Joke

# Joke Update View
class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']