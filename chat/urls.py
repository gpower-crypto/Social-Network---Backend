# chat/urls.py

from . import consumers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# I wrote this code

router = DefaultRouter()
router.register(r'chat-messages', views.ChatMessageViewSet)

urlpatterns = [
    # WebSocket URL for real-time chat
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
] + router.urls

# end of code I wrote  