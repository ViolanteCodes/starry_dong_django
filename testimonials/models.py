from django.conf import settings
from django.db import models
from django.utils import timezone


class Testimonial(models.Model):
    author = models.CharField(max_length=200)
    author_url = models.URLField(max_length=200)
    book_title = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    pull_quote = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.pull_quote