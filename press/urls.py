from django.urls import path
from . import views
from press.views import CategoryList

urlpatterns = [
    path('', CategoryList.as_view(), name='press')
]

