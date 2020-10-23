from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Testimonial

# Create your views here.

def testimonial_list(request):
    testimonials = Testimonial.objects.order_by('created_date')
    return render(request, 'testimonials.testimonial_list.html', {'testimonials': testimonials})
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})