from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(null=True, blank=True, unique=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all Reivews
        context['review_list'] = Review.objects.all()
        return context

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    """A representation of a publisher"""
    publisher_name = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.publisher_name

class Piece(models.Model):
    """A representation of a piece of fiction."""
    author = 'Maria Dong'
    category = models.ForeignKey('Category', related_name='pieces', on_delete="models.CASCADE", null=True)
    genre = models.ManyToManyField('Genre', related_name = 'pieces', blank=True)
    title = models.CharField(max_length=200)
    word_count = models.IntegerField()
    published_in = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    issue = models.CharField(max_length=200, blank=True)
    piece_url = models.URLField(blank=True)
    audio_url = models.URLField(blank=True)
    pull_quote = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    created_date = models.DateField(blank=True, null=True)
    pending_date = models.DateField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    cover_upload = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-pending_date', '-published_date']

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Review(models.Model):
    """A representation of a review in a review outlet."""
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, blank=True)
    review_url = models.URLField()
    review_venue = models.CharField(max_length=200)
    review_date = models.DateField(blank=True, null=True)
    review_pull_quote = models.CharField(max_length=200, blank=True)
    text_for_archive = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.review_pull_quote