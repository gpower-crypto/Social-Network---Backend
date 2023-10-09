from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# I wrote this code

class PostViewSetTestCase(TestCase):
    def setUp(self):
        # Create an API client
        self.client = APIClient()
        # Create a test user and authenticate the client
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    # Test creating a new post
    def test_create_post(self):
        url = '/api/posts/'
        data = {'user': self.user.id, 'text': 'Test post text'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.get()
        self.assertEqual(post.text, 'Test post text')

    # Test retrieving a list of posts
    def test_get_posts(self):
        Post.objects.create(user=self.user, text='Post 1')
        Post.objects.create(user=self.user, text='Post 2')
        url = '/api/posts/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class PostSerializerTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    # Test the serializer's ability to create a new post instance
    def test_serializer_create(self):
        serializer_data = {'user': self.user.id, 'text': 'Test post text'}
        serializer = PostSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())

        # Create a new Post instance using the serializer
        post = serializer.save()

        # Verify that the Post instance was created correctly
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.text, 'Test post text')

# end of code I wrote  