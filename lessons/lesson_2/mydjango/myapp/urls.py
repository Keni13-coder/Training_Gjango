from django.urls import path
from . import views

urlpatterns = [
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('read_db/', views.read_db, name='read_db'),
    path('creater_db/', views.creater_db, name='creater_db'),
    path('info/', views.info, name='info'),
    ]