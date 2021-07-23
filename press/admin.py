from django.contrib import admin
from press.models import Category, MediaType, Venue, PressItem

# Register your models here.

admin.site.register(Category)
admin.site.register(MediaType)
admin.site.register(Venue)
admin.site.register(PressItem)


