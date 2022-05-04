from dataclasses import fields
from re import I
from django.shortcuts import render, redirect
from accounts import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import UserFollows

def home(request):
    return render(request, 'home.html')

# @login_required

def flow(request):
    following = UserFollows.objects.filter(following=request.user)
    follower = UserFollows.objects.filter(follower=request.user)
    context = {
        'follower': follower,
        'following': following,
        'posts': Post.objects.all().order_by('-date_posted'),
    }
    ordering = ['-date_posted']

    return render(request, 'flow.html', context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'header_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'header_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

def subs(request):
    return render(request, 'subs.html')

def posts(request):
    return render(request, 'posts.html')

def review(request):
    return render(request, 'reviews/review.html')

def ticket(request):
    return render(request, 'tickets/ticket.html')

def review_of_ticket(request):
    return render(request, 'reviews/review_of_ticket.html')

def modify_ticket(request):
    return render(request, 'tickets/modify_ticket.html')

def modify_review(request):
    return render(request, 'reviews/modify_review.html')

