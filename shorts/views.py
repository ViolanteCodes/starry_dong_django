from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Piece, Publisher, Review, Genre, Category
from django.views.generic import ListView
# Create your views here.

class CategoryList(ListView):
    """View to list all pieces by category"""
    model = Category
    ordering = 'sort_order'

def shorts(request):
    unpubbed = Piece.objects.filter(published_date__isnull=True).order_by('-pending_date')
    pubbed = Piece.objects.filter(published_date__isnull=False).order_by('-published_date')
    genres = Genre.objects.all()
    reviews = Review.objects.all()
    return render(request, 'shorts/shorts.html', {'unpubbed': unpubbed, 'pubbed':pubbed, 'genres':genres, 'reviews':reviews})

def condensed(request):
    unpubbed = Piece.objects.filter(published_date__isnull=True).order_by('-pending_date')
    pubbed = Piece.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'shorts/condensed.html', {'unpubbed': unpubbed, 'pubbed':pubbed})

def by_genre(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    reviews = Review.objects.all()
    unpubbed = Piece.objects.filter(genre=genre, published_date__isnull=True).order_by('-pending_date')
    pubbed = Piece.objects.filter(genre=genre, published_date__isnull=False).order_by('-published_date')
    return render(request, 'shorts/genre_detail.html', {'unpubbed': unpubbed, 'pubbed':pubbed, 'genre':genre, 'reviews':reviews})