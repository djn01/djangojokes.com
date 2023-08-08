from django.views.generic import CreateView,  DetailView, ListView, UpdateView

from .models import Joke

# Joke Create View
class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

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