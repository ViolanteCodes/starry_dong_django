from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.publisher_name

class Piece(models.Model):
    """A representation of a piece of fiction."""
    author = 'Maria Dong'
    PIECE_TYPE_CHOICES = [
        ('story', 'Short Story'),
        ('poem', 'Poem'),
        ('essay', 'Essay'),
        ('article', 'Article')
    ]
    piece_type = models.CharField(max_length=200, choices = PIECE_TYPE_CHOICES, default='story')
    genre = models.ManyToManyField('Genre', related_name = 'pieces')
    title = models.CharField(max_length=200)
    word_count = models.IntegerField()
    published_in = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    issue = models.CharField(max_length=200, blank=True)
    piece_url = models.URLField(blank=True)
    audio_url = models.URLField(blank=True)
    pull_quote = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True, upload_to='covers')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Review(models.Model):
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