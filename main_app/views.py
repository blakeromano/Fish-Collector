from main_app.forms import FeedingForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Aquarium, Fish

from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.all()
  return render(request, 'fish/index.html', {'fish': fish})

def fish_details(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  feeding_form = FeedingForm()
  return render(request, 'fish/detail.html', {'fish': fish, 'feeding_form': feeding_form})

class FishCreate(CreateView):
  model = Fish
  fields= ['name', 'species', 'desc', 'age']

class FishUpdate(UpdateView):
  model = Fish
  fields = ['name', 'desc', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish_details', fish_id = fish_id)

class AquariumCreate(CreateView):
  model = Aquarium
  fields = '__all__'

class AquariumList(ListView):
  model = Aquarium

class AquariumDetail(DetailView):
  model = Aquarium

class AquariumUpdate(UpdateView):
  model = Aquarium
  fields = '__all__'

class AquariumDelete(DeleteView):
  model = Aquarium
  success_url = '/aquarium/'