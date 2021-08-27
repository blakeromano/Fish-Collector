from django.db import models
from django.urls import reverse

from datetime import date
# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)

class Aquarium(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=1, choices=(('F', 'Fresh Water'), ('S', 'Salt Water')))

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("aquarium_detail", kwargs={"pk": self.id})

class Fish(models.Model):
  name = models.CharField(max_length=20)
  species = models.CharField(max_length=50)
  desc = models.TextField('description', max_length=250,)
  age = models.IntegerField()
  aquariums = models.ManyToManyField(Aquarium)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fish_details', kwargs={'fish_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date = date.today()).count() >= 1

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

  