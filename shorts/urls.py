from django.urls import path
from . import views
from shorts.views import CategoryList

urlpatterns = [
    path('', CategoryList.as_view(), name='publications')
]

