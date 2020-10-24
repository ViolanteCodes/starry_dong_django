from django.contrib import admin
from .models import Publisher, Piece, Review

admin.site.register(Publisher)
admin.site.register(Piece)
admin.site.register(Review)