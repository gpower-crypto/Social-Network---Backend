from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.

# I wrote this code

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# end of code I wrote  