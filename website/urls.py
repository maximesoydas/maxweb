from importlib.resources import path
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('flow/', views.flow, name="flow"),
    path('subs/', views.subs, name="subs"),
    path('posts/', views.posts, name="posts"),
    path('review/', views.review, name="review"),
    path('ticket/', views.ticket, name="ticket"),
] 