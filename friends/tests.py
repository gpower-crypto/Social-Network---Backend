from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import FriendRequest
from users.models import UserProfile
from .serializers import FriendRequestSerializer

# I wrote this code

class FriendRequestViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='user1', password='password1')
        self.user2 = User.objects.create_user(
            username='user2', password='password2')
        self.client.force_authenticate(user=self.user1)

    def create_friend_request(self):
        # Create a friend request from user2 to user1
        return FriendRequest.objects.create(
            from_user=self.user2, to_user=self.user1, status='pending')

    def test_send_friend_request(self):
        # Test sending a friend request
        url = '/api/friend-requests/send_request/'
        data = {'to_user': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_accept_friend_request(self):
        # Test accepting a friend request
        friend_request = self.create_friend_request()
        url = f'/api/friend-requests/{friend_request.id}/accept_request/'
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reject_friend_request(self):
        # Test rejecting a friend request
        friend_request = self.create_friend_request()
        url = f'/api/friend-requests/{friend_request.id}/reject_request/'
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_friend_requests(self):
        # Create UserProfile instances for the users
        user_profile1 = UserProfile.objects.create(user=self.user1)
        user_profile2 = UserProfile.objects.create(user=self.user2)

        # Create a friend request from user2 to user1
        self.create_friend_request()

        # Test getting friend requests
        url = '/api/users/friends/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FriendRequestSerializerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user3', password='password3')
        self.user2 = User.objects.create_user(
            username='user4', password='password4')

    def test_serialize_deserialize_friend_request(self):
        # Create a FriendRequest instance
        friend_request = FriendRequest.objects.create(
            from_user=self.user1, to_user=self.user2, status='pending')

        # Serialize the FriendRequest
        serializer = FriendRequestSerializer(friend_request)

        # Deserialize the serialized data
        data = serializer.data
        deserialized_serializer = FriendRequestSerializer(data=data)

        # Check if the deserialized data is valid
        self.assertTrue(deserialized_serializer.is_valid())
        deserialized_friend_request = deserialized_serializer.save()

        # Check if the deserialized FriendRequest matches the original
        self.assertEqual(deserialized_friend_request.from_user, self.user1)
        self.assertEqual(deserialized_friend_request.to_user, self.user2)
        self.assertEqual(deserialized_friend_request.status, 'pending')

# end of code I wrote  