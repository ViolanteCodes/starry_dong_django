from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailchimp_post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]