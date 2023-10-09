# I wrote this code

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        # WebSocket route for chat sessions.
        r'ws/chat/(?P<chat_session_identifier>\w+)/$',
        consumers.ChatConsumer.as_asgi()  # Handles WebSocket connections.
    ),
]

# end of code I wrote  