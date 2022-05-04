from importlib.resources import path
from django import views
from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import follow_get
# from .views import

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="home"),
    path('flow/', views.flow, name="flow"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="ticket-detail"),
    path('subs/', follow_get, name="subs"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('posts/', views.posts, name="posts"),
    path('review/', views.review, name="review"),
    path('ticket/new/', PostCreateView.as_view(), name="ticket"),
    path('review_of_ticket/', views.review_of_ticket, name="review_of_ticket"),
    path('modify_ticket/', views.modify_ticket, name="modify_ticket"),
    path('modify_review/', views.modify_review, name="modify_review"),
    # path('<int:pk>/add', AddFollower.as_view(), name="add-follower"),
    # path('<int:pk>/remove', RemoveFollower.as_view(), name="remove-follower"),
    
] 