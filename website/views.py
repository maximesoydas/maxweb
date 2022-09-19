from django.shortcuts import render, redirect
from django.views.generic import ListView, \
    CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import UserFollows

from .forms import PostForm, ReviewForm
from django.template.defaulttags import register
from django.contrib import messages


@register.filter
# helps us loop over the review's rating and
# add stars for the range of the int variable; rating
def get_range(value):
    return range(value)


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
            print(post)
        for contact in follower:
            if post.author == contact.following:
                posts_reviews.append(post)
    for review in reviews:
        if review.author == request.user:
            posts_reviews.append(review)
        for contact in follower:
            if review.author == contact.following:
                posts_reviews.append(review)
        if review.ticket.author == request.user:
            posts_reviews.append(review)

    posts_reviews = list(set(posts_reviews))
    posts_reviews.sort(key=lambda x: x.date_posted, reverse=True)
    for p in posts_reviews:
        print(p.type)

    context = {
        'follower': follower,
        'following': following,
        'post_review': posts_reviews
    }

    return render(request, 'flow.html', context)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['ticket', 'headline', 'rating', 'content', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            return super().form_valid(form)
        except ValueError:
            messages.add_message(self.request, messages.INFO, 'Hello world.')


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
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


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['headline', 'body', 'rating']

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


def review_create_view(request):
    form2 = PostForm(request.POST, request.FILES or None)
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
        # return render(request, 'reviews/review_create.html', context)
    else:
        return render(request, 'reviews/review_create.html', context)


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
        form.save()
        return redirect('flow')
    else:

        return render(request, "website/review_form.html", context,)


def view_tickets_reviews(request):
    object1 = Post.objects.filter(author=request.user).order_by('-date_posted')
    object2 = Review.objects.filter(
        author=request.user).order_by('-date_posted')

    context = {
        'object1': object1,
        'object2': object2,
    }

    return render(request, "website/review_post_detail.html", context)
