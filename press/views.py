from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category
from django.views.generic import ListView
# Create your views here.

class CategoryList(ListView):
    """View to list all pieces by category"""
    model = Category
    ordering = 'sort_order'