from importlib.resources import path
from django import views
from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, ReviewDetailView, ReviewDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import follow_get
from .views import view_tickets_reviews,CreateReviewView, UpdateReviewView,ReviewUpdateView,ReviewCreateView,review_of_ticket,update_review

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="home"),
    path('flow/', views.flow, name="flow"),
    path('subs/', follow_get, name="subs"),
    # posts
    path('post/<int:pk>/', PostDetailView.as_view(), name="ticket-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    # path('posts/', views.posts, name="posts"),
    path('ticket/new/', PostCreateView.as_view(), name="ticket"),
#  reviews
    path('review/<int:pk>/', ReviewDetailView.as_view(), name="review-detail"),
    path('review/<int:pk>/update/', views.update_review, name="review-update"),
    path('review/<int:pk>/create_review', views.review_of_ticket, name="review-of-ticket"),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name="review-delete"),
    path('website/review_post_detail',views.view_tickets_reviews, name='posts'),
    # path('review/', views.review, name="review"),
    # path('review/new/', ReviewCreateView.as_view(), name="review"),
    path('review_create/', views.review_create_view, name="review_create"),
    path('review_of_ticket/', views.review_of_ticket, name="review_of_ticket"),
    path('modify_ticket/', views.modify_ticket, name="modify_ticket"),
    path('modify_review/', views.modify_review, name="modify_review"),
    # path('<int:pk>/add', AddFollower.as_view(), name="add-follower"),
    # path('<int:pk>/remove', RemoveFollower.as_view(), name="remove-follower"),
    
] 