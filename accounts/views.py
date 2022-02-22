from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
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