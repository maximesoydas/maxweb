from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
# from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    reviewed = models.CharField(max_length=7, default='false')
    type = models.CharField(max_length=7, default='post')

    def __str__(self):
        return str(self.title)[:30]

    def get_absolute_url(self):
        return reverse("flow")

    # class Meta:
    #     # newest at the top
    #     ordering = ('-created',)


class Review(models.Model):
    ticket = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=7, default='review')

    def __str__(self):
        return str(self.headline)[:30]

    def get_absolute_url(self):
        return reverse("flow")
