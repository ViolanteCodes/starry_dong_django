from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')
def about(request):
    return render(request, 'about.html')
def editorial(request):
    return render(request, 'editorial.html')
def fiction(request):
    return render(request, 'fiction.html')
def ubw(request):
    return render(request, 'ubw.html')