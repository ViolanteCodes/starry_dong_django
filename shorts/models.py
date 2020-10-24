from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.publisher_name

class Piece(models.Model):
    """A representation of a piece of fiction."""
    author = 'Maria Dong'
    piece_type = [
        ('story', 'Short Story'),
        ('poem', 'Poem'),
        ('essay', 'Essay'),
        ('article', 'Article')
    ] 
    title = models.CharField(max_length=200)
    word_count = models.IntegerField()
    published_in = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    issue = models.CharField(max_length=200, blank=True)
    piece_url = models.URLField(null = True)
    pull_quote = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Review(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=True)
    review_url = models.URLField()
    review_venue = models.CharField(max_length=200)
    review_date = models.DateTimeField(blank=True, null=True)
    review_pull_quote = models.CharField(max_length=200, null=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.venue