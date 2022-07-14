from enum import unique
from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username,"pk":self.pk})
        
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
    