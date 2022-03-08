
from django.conf import settings
from statistics import mode
from django.db import models
from website.models import Post
from django.contrib.auth.models import User

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     following= models.ManyToManyField(User, related_name='following', blank=True)
#     bio = models.TextField(default='no bio...')
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def profiles_posts(self):
#         return self.post_set.all()
        

#     def __str__(self):
#         return str(self.user.username)

#     class Meta:
#         # newest at the top
#         ordering = ('-created',)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    follow_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.following.username)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('following', 'follower', )