from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Testimonial

# Create your views here.

def testimonial_list(request):
    return render(request, 'testimonials/testimonial_list.html', {})