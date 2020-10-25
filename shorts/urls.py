from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorts, name='shorts'),
    path('condensed/', views.condensed, name='condensed'),
    path('genre/<genre>/', views.by_genre, name='genre'),

]

