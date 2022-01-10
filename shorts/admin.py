from django.contrib import admin
from .models import Publisher, Piece, Review, Genre, Category

admin.site.register(Publisher)
class PieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_in', 'status', 'pending_date', 'published_date')
admin.site.register(Piece, PieceAdmin)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Category)