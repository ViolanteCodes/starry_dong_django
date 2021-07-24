from django.http import HttpResponse
from django.shortcuts import render
from shorts.models import Publisher, Piece

def landing(request):
    return render(request, 'landing.html')

def about(request):
    """View to create the about me section"""
    published_list = Publisher.objects.filter(piece__published_date__isnull=False).order_by('publisher_name').distinct()
    pending_list = Publisher.objects.filter(piece__published_date__isnull=True).order_by('publisher_name').distinct()
    return render(request, 'about.html', {'published_list':published_list, 'pending_list':pending_list})

def editorial(request):
    return render(request, 'editorial.html')
def fiction(request):
    return render(request, 'fiction.html')
def ubw(request):
    return render(request, 'ubw.html')