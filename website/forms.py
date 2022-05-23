from django import forms
from .models import Review, Post

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating','content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','header_image','content', ]
        header_image = forms.ImageField()

