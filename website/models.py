from django.db import models
from accounts.models import Profile

# Create your models here.
class Ticket(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)[:30]


    class Meta:
        # newest at the top
        ordering = ('-created',)