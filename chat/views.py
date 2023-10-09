from rest_framework import viewsets, status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

# I wrote this code

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    @action(detail=False, methods=['POST'])
    def create_message(self, request):
        # Create a chat message
        user = request.user
        sender_id = user.id
        receiver_id = request.data.get('receiver_id')
        content = request.data.get('content')

        # Handle validation and response
        if not receiver_id or not content:
            return Response({'error': 'Receiver ID and content are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            chat_message = ChatMessage.objects.create(
                sender_id=sender_id,
                receiver_id=receiver_id,
                content=content
            )
            serializer = ChatMessageSerializer(chat_message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'])
    def user_chat(self, request):
        # Retrieve user chat messages
        user = request.user
        user_id = user.id
        friend_id = request.query_params.get('friend_id')

        # Query chat messages and serialize the data
        chat_messages = ChatMessage.objects.filter(
            (Q(sender=user_id, receiver=friend_id) |
             Q(sender=friend_id, receiver=user_id))
        ).order_by('timestamp')

        serializer = ChatMessageSerializer(chat_messages, many=True)
        return Response(serializer.data)

# end of code I wrote  