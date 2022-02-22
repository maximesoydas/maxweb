from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(
    max_length=200,
    required = True,
    help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
    password1 = forms.CharField(
    help_text='Enter Password',
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(
    required = True,
    help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    class Meta:
        model = User
        fields = [
        'username', 'password1', 'password2',
        ]