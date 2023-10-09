from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post

# I wrote this code

class CommentViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(user=self.user, text='Test post text')

    def test_create_comment(self):
        # Test creating a comment
        url = f'/api/comments/create_comment/?user_id={self.user.id}&post_id={self.post.id}'
        data = {'text': 'Test comment text'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get()
        self.assertEqual(comment.text, 'Test comment text')

    def test_get_comments(self):
        # Test retrieving comments
        Comment.objects.create(
            user=self.user, post=self.post, text='Comment 1')
        Comment.objects.create(
            user=self.user, post=self.post, text='Comment 2')
        url = f'/api/comments/get_comments/?user_id={self.user.id}&post_id={self.post.id}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_edit_comment(self):
        # Test editing a comment
        comment = Comment.objects.create(
            user=self.user, post=self.post, text='Original text')
        url = f'/api/comments/edit_comment/?user_id={self.user.id}&comment_id={comment.id}'
        data = {'text': 'Updated text'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertEqual(comment.text, 'Updated text')

    def test_delete_comment(self):
        # Test deleting a comment
        comment = Comment.objects.create(
            user=self.user, post=self.post, text='To be deleted')
        url = f'/api/comments/edit_comment/?user_id={self.user.id}&comment_id={comment.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)


class CommentSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.post = Post.objects.create(user=self.user, text='Test post text')

    def test_serializer_create(self):
        # Test creating a Comment instance using the serializer
        serializer_data = {
            'user': self.user.id,
            'post': self.post.id,
            'text': 'Test comment text'
        }
        serializer = CommentSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())

        # Create a new Comment instance using the serializer
        comment = serializer.save()

        # Verify that the Comment instance was created correctly
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.text, 'Test comment text')

# end of code I wrote  