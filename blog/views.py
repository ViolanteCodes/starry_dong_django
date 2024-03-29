from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Tag

# Create your views here.

def mailchimp_post_list(request):
    return render(request, 'blog/mailchimp.html')
    
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.filter(posts=post)
    return render(request, 'blog/post_detail.html', {'post': post, 'tags':tags})

