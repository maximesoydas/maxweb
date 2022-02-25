from importlib.resources import path
from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name="home"),
    path('flow/', views.flow, name="flow"),
    path('subs/', views.subs, name="subs"),
    path('posts/', views.posts, name="posts"),
    path('review/', views.review, name="review"),
    path('ticket/', views.ticket, name="ticket"),
    path('review_of_ticket/', views.review_of_ticket, name="review_of_ticket"),
    path('modify_ticket/', views.modify_ticket, name="modify_ticket"),
    path('modify_review/', views.modify_review, name="modify_review"),
] 