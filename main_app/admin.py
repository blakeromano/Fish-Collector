from main_app.models import Aquarium, Feeding, Fish
from django.contrib import admin

# Register your models here.

admin.site.register(Fish)
admin.site.register(Feeding)
admin.site.register(Aquarium)