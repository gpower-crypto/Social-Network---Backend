from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer

# Test case for the ChatMessageViewSet

# I wrote this code

class ChatMessageViewSetTestCase(TestCase):
    def setUp(self):
        # Set up an API client and user accounts
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='user1', password='password1')
        self.user2 = User.objects.create_user(
            username='user2', password='password2')
        self.client.force_authenticate(user=self.user1)

    def test_create_message(self):
        # Test creating a chat message
        url = '/api/chat-messages/create_message/'
        data = {
            'receiver_id': self.user2.id,
            'content': 'Hello, user2!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatMessage.objects.count(), 1)
        chat_message = ChatMessage.objects.get()
        self.assertEqual(chat_message.sender, self.user1)
        self.assertEqual(chat_message.receiver, self.user2)
        self.assertEqual(chat_message.content, 'Hello, user2!')

    def test_user_chat(self):
        # Test retrieving user chat messages
        chat_message1 = ChatMessage.objects.create(
            sender=self.user1, receiver=self.user2, content='Hello, user2!')
        chat_message2 = ChatMessage.objects.create(
            sender=self.user2, receiver=self.user1, content='Hi, user1!')
        url = f'/api/chat-messages/user_chat/?friend_id={self.user2.id}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

# Test case for the ChatMessageSerializer


class ChatMessageSerializerTestCase(TestCase):
    def setUp(self):
        # Create user accounts and chat message data
        self.user1 = User.objects.create_user(
            username='user1', password='password1')
        self.user2 = User.objects.create_user(
            username='user2', password='password2')
        self.chat_message_data = {
            'sender': self.user1,
            'receiver': self.user2,
            'content': 'Hello, user2!'
        }

    def test_serializer(self):
        # Test serializing a ChatMessage instance
        chat_message = ChatMessage.objects.create(**self.chat_message_data)
        serializer = ChatMessageSerializer(chat_message)
        expected_data = {
            'id': chat_message.id,
            'sender': self.user1.id,
            'receiver': self.user2.id,
            'content': 'Hello, user2!',
            'timestamp': chat_message.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
        self.assertEqual(serializer.data, expected_data)

# end of code I wrote  