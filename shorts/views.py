from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Piece, Publisher, Review, Genre
# Create your views here.

def shorts(request):
    unpubbed = Piece.objects.all()
    return render(request, 'shorts/shorts.html', {'unpubbed': unpubbed})