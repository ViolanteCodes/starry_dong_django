from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Piece, Publisher, Review, Genre, Category
from django.views.generic import ListView
# Create your views here.

def sorted_category_pieces(request):
    categories = Category.objects.all()
    pieces_list = []
    for category in categories:
        unpubbed = Piece.objects.filter(category=category, status='PEN').order_by('-pending_date')
        pubbed = Piece.objects.filter(category=category, status='PUB').order_by('-published_date')
        pieces_list.append(
            {
                'category': category,
                'unpubbed': unpubbed,
                'pubbed': pubbed,
            }
        )
    return render(request, 'shorts/category_list.html', {'pieces_list': pieces_list})

def shorts(request):
    unpubbed = Piece.objects.filter(status='PEN').order_by('-pending_date')
    pubbed = Piece.objects.filter(status='PUB').order_by('-published_date')
    genres = Genre.objects.all()
    reviews = Review.objects.all()
    return render(request, 'shorts/shorts.html', {'unpubbed': unpubbed, 'pubbed':pubbed, 'genres':genres, 'reviews':reviews})

def condensed(request):
    unpubbed = Piece.objects.filter(status='PEN').order_by('-pending_date')
    pubbed = Piece.objects.filter(status='PUB').order_by('-published_date')
    return render(request, 'shorts/condensed.html', {'unpubbed': unpubbed, 'pubbed':pubbed})

def by_genre(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    reviews = Review.objects.all()
    unpubbed = Piece.objects.filter(genre=genre, status='PEN').order_by('-pending_date')
    pubbed = Piece.objects.filter(genre=genre, status='PUB').order_by('-published_date')
    return render(request, 'shorts/genre_detail.html', {'unpubbed': unpubbed, 'pubbed':pubbed, 'genre':genre, 'reviews':reviews})