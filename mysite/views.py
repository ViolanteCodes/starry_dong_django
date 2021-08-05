from django.http import HttpResponse
from django.shortcuts import render
from shorts.models import Publisher, Piece

def landing(request):
    return render(request, 'landing.html')

def about(request):
    """View to create the about me section"""
    publisher_list = Publisher.objects.order_by('publisher_name').distinct()
    return render(request, 'about.html', {'publisher_list':publisher_list})

def editorial(request):
    return render(request, 'editorial.html')
def fiction(request):
    return render(request, 'fiction.html')
def ubw(request):
    return render(request, 'ubw.html')