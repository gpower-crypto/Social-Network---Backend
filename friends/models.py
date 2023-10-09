from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# I wrote this code

class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='friend_requests_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[(
        'pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])

    def save(self, *args, **kwargs):
        # Ensure that a user cannot send a friend request to themselves
        if self.from_user == self.to_user:
            raise ValueError(
                "A user cannot send a friend request to themselves.")
        super(FriendRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"From: {self.from_user.username}, To: {self.to_user.username}, Status: {self.status}"

# end of code I wrote  