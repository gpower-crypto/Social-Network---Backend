from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# I wrote this code

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

    def get_comments(self):
        from comments.models import Comment
        return Comment.objects.filter(post=self)

    def get_user_who_posted(self):
        return self.user
    
# end of code I wrote  