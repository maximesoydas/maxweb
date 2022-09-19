from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView,\
    PostUpdateView, PostDeleteView, ReviewDetailView,\
    ReviewDeleteView, ReviewUpdateView
from django.contrib.auth.views import LoginView
from accounts.views import follow_get

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="home"),
    path('flow/', views.flow, name="flow"),
    path('subs/', follow_get, name="subs"),
    # posts
    path('post/<int:pk>/', PostDetailView.as_view(), name="ticket-detail"),
    path(
        'post/<int:pk>/update/',
        PostUpdateView.as_view(),
        name="post-update"),
    path(
        'review/<int:pk>/update/',
        ReviewUpdateView.as_view(),
        name="review-update"),
    path(
        'post/<int:pk>/delete/',
        PostDeleteView.as_view(),
        name="post-delete"),
    path('ticket/new/', PostCreateView.as_view(),
         name="ticket"),
    path('review/<int:pk>/', ReviewDetailView.as_view(),
         name="review-detail"),
    path(
        'review/<int:pk>/create_review',
        views.review_of_ticket,
        name="review-of-ticket"),
    path(
        'review/<int:pk>/delete/',
        ReviewDeleteView.as_view(),
        name="review-delete"),
    path(
        'website/review_post_detail',
        views.view_tickets_reviews,
        name='posts'),
    path('review_create/', views.review_create_view,
         name="review_create"),

]
