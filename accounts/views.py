from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .models import Profile
from django.views.generic import ListView, DetailView

from accounts.models import UserFollows
# from accounts.models import Profile
from .forms import RegisterForm
# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User

# Create your views here.


def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form = AuthenticationForm(request)
            form.fields['username'].widget.attrs.update({
                'placeholder': 'Name'
            })
            form.fields['password'].widget.attrs.update({
                'placeholder': 'Password'
            })

            context = RequestContext(request, {
                'form': form,
            })
            return HttpResponse(template.render(context))
    else:
        form = UserCreationForm
    return render(request, 'registration/register.html', {'form': form})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('home')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'register.html', context)


class ProfileListView(ListView):
    model = User
    template_name = 'subs.html'
    context_object_name = 'profiles'


def follow_get(request):
    following = UserFollows.objects.filter(following=request.user)
    follower = UserFollows.objects.filter(follower=request.user)
    context = {
        'follower': follower,
        'following': following
    }
    return render(request, 'subs.html', context)

# check for error
def delete_userfollow(request, id):
    if request.method == 'POST':
        print(id)
        print("Username")
        print(request.user.id)
        if id == request.user.id:
            pi = UserFollows.objects.filter(following=id)
            pi.delete()
        else:
            pi = UserFollows.objects.filter(following=id)
            pi.delete()
        return redirect('subs')


@login_required
def search_bar(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        try:
            user_to_follow = User.objects.get(username=search_query)
            userfollow = UserFollows.objects.create(
                following=user_to_follow, follower=request.user)
        except Exception as e:
            print(e)

        return redirect('subs')
