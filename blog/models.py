from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Tag(models.Model):
    """A blog tag"""
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Post(models.Model):
    """A blog post"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name ='posts')
    title = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title