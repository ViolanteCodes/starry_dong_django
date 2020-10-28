from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorts, name='shorts'),
    path('condensed/', views.condensed, name='condensed'),
    path('genre/<slug:slug>/', views.by_genre, name='genre'),

]

