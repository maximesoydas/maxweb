from importlib.resources import path
from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import ProfileListView

urlpatterns = [
    path('', LoginView.as_view(), name="home"),
    path('flow/', views.flow, name="flow"),
    path('subs/', ProfileListView.as_view(), name="subs"),
    path('posts/', views.posts, name="posts"),
    path('review/', views.review, name="review"),
    path('ticket/', views.ticket, name="ticket"),
    path('review_of_ticket/', views.review_of_ticket, name="review_of_ticket"),
    path('modify_ticket/', views.modify_ticket, name="modify_ticket"),
    path('modify_review/', views.modify_review, name="modify_review"),
    # path('<int:pk>/add', AddFollower.as_view(), name="add-follower"),
    # path('<int:pk>/remove', RemoveFollower.as_view(), name="remove-follower"),
    
] 