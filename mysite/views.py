from django.http import HttpResponse
from django.shortcuts import render



#DataFlair #Views #TemplateInheritance
# Create your views here.
# def home(request):
#     return render(request, 'base.html')
# def other(request):
#     context = {
#     'k1': 'Welcome to the Second page',
#     }
#     return render(request, 'others.html', context)
def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')
