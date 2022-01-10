from django.urls import path
from . import views
from shorts.views import sorted_category_pieces

urlpatterns = [
    path('', sorted_category_pieces, name='publications')
]

