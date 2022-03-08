from multiprocessing import context
from django.shortcuts import render,redirect
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
    return render(request,'index.html')
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

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
                'form' : form,
            })
            return HttpResponse(template.render(context))
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm
    return render(request,'registration/register.html', {'form':form})

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
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

    return render(request, 'register.html', {})


class ProfileListView(ListView):
    model = User
    template_name = 'subs.html'
    context_object_name = 'profiles'
    

def follow_get(request):
    following = UserFollows.objects.filter(following=request.user)
    followers = UserFollows.objects.filter(follower=request.user)
    context = {
         'followers':followers,
         'following':following
         }
    return render(request, 'subs.html', context)
    
@login_required
def search_bar(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        try:
            user_to_follow = User.objects.get(username= search_query)
            userfollow = UserFollows.objects.create(following=user_to_follow, follower=request.user)
        except Exception as e:
            print(e)
            
        return redirect('subs')
        '''
        YourModel = Model where you want to run search
        attibute = attribute on your model where you want to run search
        search_results.html = is a seperate page where your search results will be displayed.
        '''    
# def follow_unfollow_profile(request):

#     if request.method=="POST":
#         my_profile = Profile.objects.get(user=request.user)
#         pk = request.POST.get('profile_pk')
#         obj = Profile.objects.get(pk=pk)

#         if obj.user in my_profile.following.all():
#             my_profile.following.remove(obj.user)
#         else:
#             my_profile.following.add(obj.user)
#         return redirect(request.META.get('HTTP_REFERER'))
#     return redirect('profile-list-view')



# def searchbar(self, request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         username = Profile.objects.all().exclude(user=self.request.user)
#         return render(request,'searchbar.html', {'username': username})


# class ProfileView(View):
#     def get(self, request, pk, *args, **kwargs):

#         profile = Profile.objects.get(pk=pk)
#         user= profile.user
#         followers = profile.followers.all()

#         if len(followers) == 0:
#             is_following = False

#         for follower in followers:
#             if follower == request.user:
#                 is_following = True
#                 break
#             else:
#                 is_following = False

#         print(user)

#         context = {
#             'user': user,
#             'followers':followers,
#             'is_following': is_following,
#         }
#         print(context)
#         return render(request, 'subs.html', context)



# class AddFollower(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         profile = Profile.objects.get(pk=pk)
#         profile.followers.add(request.user)
#         print(profile.pk)
#         print(profile.followers.all())

#         return redirect('subs')

# class RemoveFollower(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         profile = User.objects.get(pk=pk)
#         profile.follower.remove(request.user)

#         return redirect('subs')





# class ProfileDetailView(DetailView):
#     model = Profile
#     template_name = 'profiles/detail.html'

#     def get_object(self, **kwargs):
#         pk = self.kwargs.get('pk')
#         view_profile = Profile.objects.get(pk=pk)
#         return view_profile

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         view_profile = self.get_object()
#         my_profile = Profile.objects.get(user=self.request.user)
#         if view_profile.user in my_profile.following.all():
#             follow = True
#         else:
#             follow = False
#         context["follow"] = follow


#         return context
