from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer

# I wrote this code

class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()

    def create_user_profile(self):
        # Create a user profile for the current user
        return UserProfile.objects.create(
            user=self.user, name="Test User", bio="Test Bio", location="Test Location", status="Initial status"
        )

    def test_register(self):
        # Test user registration
        url = "/api/users/register/"
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_friends(self):
        # Test getting a user's friends
        url = "/api/users/friends/"
        self.client.force_authenticate(user=self.user)

        # Create a UserProfile for the user
        user_profile = self.create_user_profile()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_profile(self):
        # Test creating a user profile
        url = "/api/users/create_profile/"
        self.client.force_authenticate(user=self.user)
        data = {"name": "New Name", "bio": "New Bio",
                "location": "New Location"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assuming you start with one profile
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_edit_profile(self):
        # Test editing a user profile
        url = f"/api/users/{self.user.id}/edit_profile/"
        self.client.force_authenticate(user=self.user)
        data = {"bio": "Updated Bio"}

        # Create a UserProfile for the user
        user_profile = self.create_user_profile()

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_profile.refresh_from_db()
        self.assertEqual(user_profile.bio, "Updated Bio")

    def test_get_profile(self):
        # Test getting a user's profile
        url = f"/api/users/{self.user.id}/get_profile/"
        self.client.force_authenticate(user=self.user)

        # Create a UserProfile for the user
        user_profile = self.create_user_profile()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status(self):
        # Test getting a user's status
        url = "/api/users/status/"
        self.client.force_authenticate(user=self.user)

        # Create a UserProfile for the user
        user_profile = self.create_user_profile()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_status(self):
        # Test updating a user's status
        url = "/api/users/update_status/"
        self.client.force_authenticate(user=self.user)
        data = {"status": "Updated status"}

        # Create a UserProfile for the user
        user_profile = self.create_user_profile()

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_profile.refresh_from_db()
        self.assertEqual(user_profile.status, "Updated status")

# Test case for the UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user_serializer = UserSerializer(data=self.user_data)
        self.assertTrue(self.user_serializer.is_valid())
        self.user_serializer.save()

    def test_user_serializer(self):
        user = User.objects.get(username='testuser')
        serialized_data = UserSerializer(user).data
        self.assertEqual(serialized_data['username'], 'testuser')
        self.assertTrue('password' not in serialized_data)

# Test case for the UserProfileSerializer


class UserProfileSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user_serializer = UserSerializer(data=self.user_data)
        self.assertTrue(self.user_serializer.is_valid())
        self.user_serializer.save()

        self.user = User.objects.get(username='testuser')

        # Create UserProfile for the user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            name='Test User',
            bio='Test Bio',
            location='Test Location',
        )

    def test_profile_serializer(self):
        serialized_data = UserProfileSerializer(self.user_profile).data
        self.assertEqual(serialized_data['name'], 'Test User')
        self.assertEqual(serialized_data['bio'], 'Test Bio')
        self.assertEqual(serialized_data['location'], 'Test Location')

# end of code I wrote  