import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# Import the WebSocket URLs from the chat app
from chat.routing import websocket_urlpatterns

# I wrote this code

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_SocialNetwork.settings')

# Get the ASGI application
django_asgi_app = get_asgi_application()

# Define the ProtocolTypeRouter for handling different protocols
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # For regular HTTP requests
    "websocket": URLRouter(websocket_urlpatterns),  # For WebSocket handling
})

# end of code I wrote  