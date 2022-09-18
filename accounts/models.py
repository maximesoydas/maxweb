from django.db import models
from django.contrib.auth.models import User


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following")
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower")
    follow_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.following.username)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('following', 'follower', )
