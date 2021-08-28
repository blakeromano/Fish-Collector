from main_app.forms import FeedingForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Aquarium, Fish
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(LoginView):
  template_name='home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fish_index(request):
  fish = Fish.objects.filter(user = request.user)
  return render(request, 'fish/index.html', {'fish': fish})

@login_required
def fish_details(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  aquariums_fish_doesnt_have = Aquarium.objects.exclude(id__in = fish.aquariums.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fish/detail.html', {'fish': fish, 'feeding_form': feeding_form, 'aquariums': aquariums_fish_doesnt_have,})


class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields= ['name', 'species', 'desc', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = ['name', 'desc', 'age']

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fish/'

@login_required
def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish_details', fish_id = fish_id)


class AquariumCreate(LoginRequiredMixin, CreateView):
  model = Aquarium
  fields = '__all__'

class AquariumList(LoginRequiredMixin, ListView):
  model = Aquarium

class AquariumDetail(LoginRequiredMixin, DetailView):
  model = Aquarium

class AquariumUpdate(LoginRequiredMixin, UpdateView):
  model = Aquarium
  fields = '__all__'

class AquariumDelete(LoginRequiredMixin, DeleteView):
  model = Aquarium
  success_url = '/aquarium/'

@login_required
def assoc_aquarium(request, fish_id, aquarium_id):
  Fish.objects.get(id=fish_id).aquariums.add(aquarium_id)
  return redirect('fish_details', fish_id = fish_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)