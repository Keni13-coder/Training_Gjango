from django.urls import path
from . import views

urlpatterns = [
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('the_dice/', views.the_dice, name='the_dice'),
    path('random_numbers/', views.random_numbers, name='random_numbers'),
]