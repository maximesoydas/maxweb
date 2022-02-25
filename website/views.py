from django.shortcuts import render, redirect
from accounts import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

# @login_required

def flow(request):
    return render(request, 'flow.html')

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
