from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Piece, Publisher, Review, Genre
# Create your views here.

def shorts(request):
    unpubbed = Piece.objects.filter(published_date__isnull=True).order_by('-created_date')
    pubbed = Piece.objects.filter(published_date__isnull=False).order_by('-published_date')
    genres = Genre.objects.all()
    return render(request, 'shorts/shorts.html', {'unpubbed': unpubbed, 'pubbed':pubbed, 'genres':genres})

def condensed(request):
    unpubbed = Piece.objects.filter(published_date__isnull=True).order_by('-created_date')
    pubbed = Piece.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'shorts/condensed.html', {'unpubbed': unpubbed, 'pubbed':pubbed})

def by_genre(request, genre):
    genre = get_object_or_404(Genre, name=genre)
    stories = genre.objects.all()
    return render(request, 'shorts/genre_detail.html', {'stories': stories})