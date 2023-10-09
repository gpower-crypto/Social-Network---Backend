from django.db import models
from django.contrib.auth.models import User
from friends.models import FriendRequest
# Create your models here.

# I wrote this code

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_friends(self):
        # Return a list of friends for the user
        friends = []
        friend_requests = FriendRequest.objects.filter(status='accepted').filter(
            models.Q(from_user=self.user) | models.Q(to_user=self.user))
        for request in friend_requests:
            if request.from_user == self.user:
                friends.append(request.to_user)
            else:
                friends.append(request.from_user)
        return friends

    def get_friend_requests_received(self):
        # Return a list of friend requests received by this user
        return FriendRequest.objects.filter(to_user=self.user, status='pending')

    def get_friend_requests_sent(self):
        # Return a list of friend requests sent by this user
        return FriendRequest.objects.filter(from_user=self.user, status='pending')

# end of code I wrote  