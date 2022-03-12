from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    """A type of press item, used for list sorting"""
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    """A representation of a venue for press item"""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class MediaType(models.Model):
    """A list of media types"""
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PressItem(models.Model):
    """A representation of a press item."""
    author = 'Maria Dong'
    category = models.ForeignKey(
        'Category', related_name='press_items', on_delete = models.CASCADE, null=True
    )
    media_type = models.ForeignKey(
        'MediaType', related_name='press_items', on_delete = models.CASCADE
    )
    title = models.CharField(max_length=200)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    published_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title