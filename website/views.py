from dataclasses import fields
from re import I
from django.shortcuts import render, redirect
from accounts import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from .models import Post, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import UserFollows
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from itertools import zip_longest
import operator
from operator import itemgetter
from .forms import PostForm, ReviewForm

def home(request):
    return render(request, 'home.html')

# @login_required

def flow(request):
    following = UserFollows.objects.filter(following=request.user)
    follower = UserFollows.objects.filter(follower=request.user)
    posts = [] 
    reviews = []
    for post in Post.objects.all().order_by('-date_posted'):
        posts.append(post)
    for review in Review.objects.all().order_by('-date_posted'):
        reviews.append(review)

    posts_reviews = []

    for post in posts:
        if post.author == request.user:
            posts_reviews.append(post)
        for contact in follower:
            if post.author == contact.following:
                posts_reviews.append(post)
    for review in reviews:
        if review.author == request.user:
            posts_reviews.append(review)
        for contact in follower:
            if review.author == contact.following:
                posts_reviews.append(review)

    posts_reviews.sort(key=lambda x: x.date_posted, reverse=True)
    # print(post_reviews)
    
    
    
    for p in posts_reviews:
      print(p.type)
      

    context = {
        'follower': follower,
        'following': following,
        'post_review': posts_reviews
    }

    return render(request, 'flow.html', context)


class ReviewMetaInline(InlineFormSetFactory):
    model = Review
    fields = ['ticket','rating', 'headline', 'content',]
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': False}
    formset_kwargs = {'auto_id': 'my_id_%s'}

class CreateReviewView(CreateWithInlinesView):
    model = Post
    inlines = [ReviewMetaInline]
    fields = ['title', 'content', 'header_image']
    template_name = 'website/review_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

class UpdateReviewView(UpdateWithInlinesView):
    model = Post
    inlines = [ReviewMetaInline]
    fields = ['title', 'content', 'header_image']
    template_name = 'website/review_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return self.object.get_absolute_url()

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = [ 'ticket', 'headline','rating', 'content',]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = [ 'ticket', 'headline','rating', 'content',]
    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        print('R')
        return super().form_valid(form)
    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False

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
        self.object = form.save()
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

class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class ReviewDetailView(DetailView):
    model = Review

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

def review_create_view(request):
    form2 = PostForm(request.POST,request.FILES or None)
    form = ReviewForm(request.POST or None)

    context = {

        "form2": form2,
        "form": form,
    }
    
    if all([form2.is_valid(), form.is_valid()]):
        current_user = request.user
        parent = form2.save(commit=False)
        parent.author_id = current_user.id
        parent.reviewed = 'true'
        parent.save()
        child = form.save(commit=False)
        child.author_id = current_user.id
        child.ticket = parent
        child.save()
        print("form", form.cleaned_data)
        print("form2", form2.cleaned_data)
        context['message'] = 'data saved'

        return redirect('flow')

    return render(request, "reviews/review_create.html", context,)

def update_review(request, pk): 
    instance = Review.objects.get(id=pk)
    form = ReviewForm(request.POST or None, instance=instance)
    review_form = form.save(commit=False)
    review_form_ticket = review_form.ticket
    context = {
        "form": form,
        "ticket": review_form_ticket,
    }
    if form.is_valid():
          form.save()
          return redirect('flow')
    
    return render(request, "website/review_form.html", context,)


def review_of_ticket(request, pk): 
    
    instance = Post.objects.get(id=pk)
    form = ReviewForm(request.POST or None)
    review_form_ticket = instance
    context = {
        "form": form,
        "ticket": review_form_ticket,
    }
    if form.is_valid():
        current_user = request.user
        child = form.save(commit=False)
        child.author_id = current_user.id
        child.ticket = instance
        instance.reviewed = 'true'
        child.save()
        instance.save()
        print(instance.reviewed)
        form.save()
        return redirect('flow')

    return render(request, "website/review_form.html", context,)