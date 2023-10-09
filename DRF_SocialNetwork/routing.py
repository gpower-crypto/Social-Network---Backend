from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include

# I wrote this code

# Import the WebSocket URLs
from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns

application = ProtocolTypeRouter({
    # Use the WebSocket URLs from the chat app
    "websocket": URLRouter(chat_websocket_urlpatterns),
})

# end of code I wrote  