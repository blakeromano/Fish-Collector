from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
  path('',  views.home, name='home'),
  path('about/', views.about, name='about'),
  path("fish/", views.fish_index, name='index'),
  path('fish/<int:fish_id>/', views.fish_details, name='fish_details'),
  path('fish/create', views.FishCreate.as_view(), name='fish_create'),
  path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
  path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
  path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('aquarium/create/', views.AquariumCreate.as_view(), name='aquarium_create'),
  path('aquarium/', views.AquariumList.as_view(), name='aquarium_index'),
  path('aquarium/<int:pk>', views.AquariumDetail.as_view(), name='aquarium_detail'),
  path('aquarium/<int:pk>/update/', views.AquariumUpdate.as_view(), name='aquarium_update'),
  path('aquarium/<int:pk>/delete/', views.AquariumDelete.as_view(), name='aquarium_delete')
]